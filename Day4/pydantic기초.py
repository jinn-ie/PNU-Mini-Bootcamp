from pydantic import BaseModel

class Addr(BaseModel):
    country: str
    city: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    addr: Addr | None = None # Addr 클래스를 포함

class Shop(BaseModel):
    id: int
    name: str
    addr: Addr

user = User(id=1, name="Lee", email="lee@naver.com")


print(user.model_dump_json())   # JSON 형태로 변환
print(user.model_dump())        # Dict 형태로 변환

userDict = {
    "id": 2,
    "name": "Park",
    "email": "park@naver.com"
}      
print(User(**userDict))         # Dict -> Model
str_user_json = '{"id": 3, "name": "Kim", "email": "kim@naver.com"}'
print(User.model_validate_json(str_user_json))  # JSON -> Model

# Callable : 함수 메소드
from typing import Callable
class Methods(BaseModel):
    func: Callable[[int], str] # in: int, out: str

def int_to_str(val: int) -> str:
    return f'{val}'

m = Methods(func=int_to_str)
print(type(m.func(123)))