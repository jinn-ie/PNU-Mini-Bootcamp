from fastapi import FastAPI, Depends, HTTPException
from dataclasses import dataclass, asdict 
import time
from sqlmodel import (
    Field, SQLModel, Session,
    create_engine, select
)

#from app.services.post_service import *

# id, created_at은 직접 입력하기 어려움
# dataclass로 필요한 값만 입력받아서 처리
@dataclass
class PostReq:
    title: str
    body: str
    published: bool

# db 테이블 정의
class Post(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    created_at: int = Field(index=True)
    published: bool = Field(index=True)
    title: str
    body: str

# 명확한 형식, 에러 메시지 확장 가능
@dataclass
class PostsResp:
    posts: list[Post]
    err: str | None = None

# db 연결 설정
db_url = "sqlite:///Day3/blog.db" # 파일명
db_engine = create_engine(db_url, connect_args={"check_same_thread": False}) # 다중 스레드 접근

# db 세션 설정 (커밋, 롤백 객체)
def get_db_session():
    # session = Session(db_engine)
    # return session
    with Session(db_engine) as session:
        yield session

# 모든 SQLModel 클래스에 대해 테이블을 생성
def create_db():
    SQLModel.metadata.create_all(db_engine)

app = FastAPI()

create_db()

# 게시글 생성
@app.post("/posts")
def create_post(post: PostReq,
               db = Depends(get_db_session)):
    
# def create_post(post: PostReq,
#                 db = Depends(get_db_session),
#                 postService = Depends()):
    
    # resp = postService.create_post(db, post)
    
    postModel = Post()
    postModel.title= post.title
    postModel.body = post.body
    postModel.published = post.published
    postModel.created_at = int(time.time())
    
    db.add(postModel)
    db.commit()
    db.refresh(postModel) # db에 저장된 데이터를 다시 가져옴 (id, created_at)
    return postModel

# 게시글 목록 조회
@app.get("/posts")
def get_posts(page: int=1, limit: int=2,
              db = Depends(get_db_session)):
    if page < 1: page = 1
    if limit < 1: return []
    if limit > 2: limit = 2

    nOffset = (page - 1) * limit
    # select로 쿼리 가져옴 -> 실행 및 결과 리스트 반환
    posts = db.exec(select(Post).offset(nOffset).limit(limit)).all()

    # 관리하기 더 편함
    resp = PostsResp(posts=posts)
    return resp


# 게시글 조회
@app.get("/posts/{post_id}")
def get_post(post_id: int,
             db = Depends(get_db_session)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    resp = PostsResp(posts=[post]) # 데이터 형식 유지
    return resp

# 게시글 삭제
@app.delete("/posts/{post_id}")
def delete_post(post_id: int,
                db=Depends(get_db_session)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {
        'ok': True
    }

# 게시글 수정
@app.put("/posts/{post_id}")
def update_post(post_id: int, reqBody: PostReq,
                db=Depends(get_db_session)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # dataclass -> dict
    dictToUpdate = asdict(reqBody)
    post.sqlmodel_update(dictToUpdate)
    db.add(post)
    db.commit()
    db.refresh(post)

    resp = PostsResp(posts=[post])
    return resp

# ctrl + shift + p -> sqlite3
# sqlite> open database
# 좌측 하단 SQLite Explorer

# fastapi dev Day3/database.py