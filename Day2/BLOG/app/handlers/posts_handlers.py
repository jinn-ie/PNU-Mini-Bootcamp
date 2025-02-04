from fastapi import APIRouter
import time
from app.models.post import *
from app.models.shared import *

router = APIRouter(prefix="/v1/posts")

# 게시글 목록 조회
@router.get("/")
def get_posts(dir: PageDir=PageDir.NEXT,
              post_id: int=0, limit: int=10) -> PostsResp:
    
    ###

    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post(
                id=1,
                title="T",
                body="B",
                created_at=nCurTimestamp,
                published=True
            ),
            Post(
                id=2,
                title="TT",
                body="BB",
                created_at=nCurTimestamp,
                published=True
            )
        ]
    )

# 특정 게시글 조회
@router.get("/{post_id}")
def get_post(post_id: int) -> PostsResp:
    
    ###

    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post(
                id=1,
                title="T",
                body="B",
                created_at=nCurTimestamp,
                published=True
            )
        ]
    )

# 게시글 작성
@router.post("/")
def create_post(params: CreatePostReq) -> PostsResp:
    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post(
                id=999,
                title=params.title,
                body=params.body,
                created_at=nCurTimestamp,
                published=params.publish
            )
        ]
    )

# 게시글 수정
@router.put("/{post_id}")
def update_post(post_id: int, params: UpdatePostReq) -> PostsResp:
    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post( # None이면 업데이트 안 하나?
                id=999,
                title=params.title,
                body=params.body,
                created_at=nCurTimestamp,
                published=params.publish
            )
        ]
    )

# 게시글 삭제
@router.delete("/{post_id}")
def delete_post(post_id: int) -> ResultReq:
    return ResultReq(ok=True)