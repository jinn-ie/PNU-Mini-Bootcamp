
from dataclasses import dataclass
from sqlmodel import Session

@dataclass
class PostReq:
    title: str
    body: str
    published: bool

class PostService:
    def get_post(self, db: Session, post_id: int):
        pass

    def get_posts(self, db: Session, page: int=1):
        pass

    def create_post(self, db: Session, post: PostReq):
        pass

    def update_post(self, db: Session,
                    post_id: int, post: PostReq):
        pass

    def delete_post(self, db: Session, post_id: int):
        pass