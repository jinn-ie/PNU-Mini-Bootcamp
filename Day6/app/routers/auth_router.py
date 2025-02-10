from fastapi import APIRouter, Depends, HTTPException
from app.models.parameter_models import AuthSignupReq, AuthSigninReq
from app.dependencies.db import get_db_session
from app.dependencies.jwt_utils import JwtUtil
from app.services.auth_service import AuthService

router = APIRouter(prefix='/auth')

# 1. signup
@router.post('/signup')
def auth_signup(req: AuthSignupReq,
                db=Depends(get_db_session),         # 함수 가져올때 이렇게
                jwtUtil: JwtUtil=Depends(),         # class 가져올때 이렇게
                authService: AuthService=Depends()):
    user = authService.signup(db, req.login_id, req.pwd, req.name)
    if not user:
        raise HTTPException(status_code=400, detail='Signup Failed')
    user.access_token = jwtUtil.create_token(user.model_dump())
    return user

# 2. signin
@router.post('/signin')
def auth_signin(req: AuthSigninReq,
                db=Depends(get_db_session),
                jwtUtil: JwtUtil=Depends(),
                authService: AuthService=Depends()):
    user = authService.signin(db, req.login_id, req.pwd)
    if not user:
        raise HTTPException(status_code=401, detail='Signin Failed')
    user.access_token = jwtUtil.create_token(user)
    return user