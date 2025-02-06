from fastapi import FastAPI, HTTPException, status, Depends
from dataclasses import dataclass

app = FastAPI()

@dataclass
class SigninReq:
    login_id: str
    password: str

# 제약조건
def validate_signin(req: SigninReq) -> SigninReq:
    if len(req.login_id) < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Length of password 4~12"
        )
    return req

# 의존성 주입
@app.post("/auth/login")
def auth_login(user: SigninReq=Depends(validate_signin)):
    return user