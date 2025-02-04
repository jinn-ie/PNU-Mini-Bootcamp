from dataclasses import dataclass

# 많이 쓰는 패턴이라 shared에 넣어놓음
@dataclass
class ResultReq:
    ok: bool = False
    err_msg: str | None = None