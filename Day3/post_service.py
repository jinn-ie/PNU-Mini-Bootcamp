
from dataclasses import dataclass
from sqlmodel import (
    Field, SQLModel,
    Session, select
)
import time

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

class PostService:
    def create_post(self, db: Session, req: PostReq):
                
        post = Post()
        post.title= req.title
        post.body = req.body
        post.published = req.published
        post.created_at = int(time.time())
        
        db.add(post)
        db.commit()
        db.refresh(post) # db에 저장된 데이터를 다시 가져옴 (id, created_at)
        
        return post

    def get_posts(self, db: Session, page: int=1, limit: int=10):
        nOffset = (page - 1) * limit

        # select로 쿼리 가져옴 -> 실행 및 결과 리스트 반환
        posts = db.exec(
            select(Post).offset(nOffset).limit(limit)
            ).all()

        return posts

    def get_post(self, db: Session, post_id: int):
        
        post = db.get(Post, post_id)
        return post

    def update_post(self, db: Session,
                    post_id: int, req: PostReq):
        pass

    def delete_post(self, db: Session, post_id: int) -> bool:
        post = db.get(Post, post_id)
        if not post:
            return False
        db.delete(post)
        db.commit()
        return True