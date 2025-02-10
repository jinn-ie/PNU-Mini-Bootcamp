from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY='1234'
ALG = 'HS256'

class JwtUtil:
    # 1. JWT Token 생성 함수
    def create_token(self, payload: dict,
                     expires_delta: timedelta | None = timedelta(minutes=30)):
        payload_to_encode = payload.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        payload_to_encode.update({
            "exp": expire
        })
        return jwt.encode(payload_to_encode, SECRET_KEY, algorithm=ALG)
    
    def decode_token(self, token: str):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALG])
    
if __name__ == '__main__':
    payload = {
        'id': 1,
        'name': 'Linux',
        'login_id': 'loiss'
    }
    jwtUtil = JwtUtil()
    token = jwtUtil.create_token(payload=payload, expires_delta=timedelta(minutes=5))
    print(token)

    payload2 = jwtUtil.decode_token(token)
    print(payload2)