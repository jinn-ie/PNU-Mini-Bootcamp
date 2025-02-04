from fastapi import FastAPI
from enum import Enum
from dataclasses import dataclass

app = FastAPI()

# 데이터구조 정의 후 params로 받아서 사용
@dataclass
class SignupParams:
    login_id: str
    password: str
    name: str
    age: int

@dataclass
class AuthResp:
    jwt_token: str
    err_msg: str | None = None

@dataclass
class SigninParams:
    login_id: str
    password: str

@dataclass
class Post:
    id: int
    title: str

@dataclass
class PostResp:
    posts = list[Post]
    err: str | None = None

class CarType(Enum):
    BUS = "bus"
    SUV = "suv"
    TANK = "tank"

# 라우트 기본
@app.get('/')
def root():
    return {"message": "msg"}

@app.get('/hello')
def hello():
    return {"message": "Hello World"}

# path parameter - 필수
@app.post('/hello/{num}')
def hello(num : int):
    return {'result': num * 10}    

@app.get('/car/{car_type}')
def get_car(car_type: CarType):
    return {"car_type": car_type}

# 같은 형식일 때 위의 것 먼저 적용
@app.get('posts/comments')
def hello():
    return {'result' : 'comments'}
@app.get('/posts/{num}')
def hello(num : int):
    return {'result': num * 10}

# query parameter - 선택
# ?q=apple
@app.get("/products")
def get_products(q : str | None = None):
    products = {"products" : [{"name" : "apple"}, {"name" : "banana"}]}
    if q:
        products.update({"q" : q})
    return products

# request body - 필수, POST/PUT
# login : POST (GET은 URL에 노출)
# raw data - json
@app.post('/auth/signup')
def signup(params: SignupParams) -> AuthResp:
    return AuthResp(jwt_token="1234")

@app.post('/auth/signin')
def signin(params: SigninParams) -> AuthResp:
    #token = generate_token()
    return AuthResp(jwt_token="token")

# .venv/Scripts/activate
# fastapi dev Day2/fastAPI.py