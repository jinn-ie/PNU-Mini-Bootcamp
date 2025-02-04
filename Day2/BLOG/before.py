from fastapi import FastAPI
from enum import Enum
from dataclasses import dataclass
from typing import Optional
import time

app = FastAPI()

class PageDir(Enum):
    NEXT = "next"
    PREV = "prev"

@dataclass
class User:
    login_id: str
    password: str
    name: str

@dataclass
class Post:
    id: int
    title: str
    body: str
    created_at: int
    published: bool

@dataclass
class AuthLoginReq:
    login_id: str
    password: str

@dataclass
class AuthResponse:
    jwt_token: str | None = None
    err_msg: str | None = None

@dataclass
class PostsResp:
    posts: list[Post]
    err_msg: str | None = None

@dataclass
class CreatePostReq:
    title: str
    body: str
    publish: bool = False

@dataclass
class UpdatePostReq:
    title: Optional[str] = None
    body: Optional[str] = None
    publish: Optional[bool] = False

@dataclass
class ResultReq:
    ok: bool = False
    err_msg: Optional[str] = None



@app.post("/auth/signup")
def signup(user: User) -> AuthResponse:
    return AuthResponse(
        jwt_token="sksksksks"
    )

@app.post("/auth/signin")
def signin(user: AuthLoginReq) -> AuthResponse:
    return AuthResponse(
        jwt_token='aaaa'
    )

@app.get("/posts")
def get_posts(dir: PageDir=PageDir.PREV, 
              post_id: int=0, 
              limit: int=30) -> PostsResp:
    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post(id=1, title="T",body="B",
                 created_at=nCurTimestamp,
                 published=True),
            Post(id=2, title="TT",body="B1",
                 created_at=nCurTimestamp,
                 published=True)
        ]
    )


@app.get("/posts/{post_id}")
def get_post(post_id: int) -> PostsResp:
    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post(id=post_id, title="T",body="B",
                 created_at=nCurTimestamp,
                 published=True)
        ]
    )

@app.post("/posts")
def create_post(params: CreatePostReq) -> PostsResp:
    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post(id=999, title=params.title,
                 body=params.body,
                 created_at=nCurTimestamp,
                 published=params.publish)
        ]
    )

@app.put("/posts/{post_id}")
def update_post(post_id: int, params: UpdatePostReq) ->PostsResp:
    nCurTimestamp = int(time.time())
    return PostsResp(
        posts=[
            Post(id=post_id, title=params.title,
                 body=params.body,
                 created_at=nCurTimestamp,
                 published=params.publish)
        ]
    )

@app.delete("/posts/{post_id}")
def delete_post(post_id: int) -> ResultReq:
    return ResultReq(ok=True)