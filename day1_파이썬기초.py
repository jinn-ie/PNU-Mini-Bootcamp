
# dataclass를 사용하여 인자의 타입 만들기
from dataclasses import dataclass

# Enum을 사용하여 문자열을 상수로 만들기
from enum import Enum

@dataclass

class User:
    loginId: str
    name: str
    age: int
    email: str

class ProductCategory(Enum):
    ELECTRONICS = 'electronics'
    CLOTHING = 'clothing'
    HOME = 'home'

db = ['Linux', 'Windows', 'MacOS', 'Ubuntu', 'Redhat']

def get_products(page: int=1, per_page: int=2) -> list | None:
    if type(page) != int:
        return None
    start = (page-1) * per_page
    end = start + per_page
    return db[start:end]
