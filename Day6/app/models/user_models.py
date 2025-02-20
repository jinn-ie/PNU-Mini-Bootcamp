from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: int | None = Field(index=True)
    login_id: str = Field(index=True)
    pwd: str = Field(default=None, exclude=True) # exclude: 백엔드 내부에서만 사용, 사용자에게 제공 X
    name: str
    access_token: str | None = None
    