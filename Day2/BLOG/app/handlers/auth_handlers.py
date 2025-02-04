from fastapi import APIRouter
from app.models.user import *
#from app.models.shared import *

# version1, 공통 prefix로 라우팅
router = APIRouter(prefix="/v1/auth")

# 회원가입
# @app.post("/auth/signup")
@router.post("/signup")
def signup(user: User) -> AuthResp:
    ### TODO ###

    return AuthResp(
        jwt_token="7985494138"
    ) 

# 로그인
@router.post("/signin")
def signin(user: AuthLoginReq) -> AuthResp:
    ### TODO ###

    return AuthResp(
        jwt_token="7985494138"
    )