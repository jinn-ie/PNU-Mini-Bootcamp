from socket import *
import re # 정규표현식
import json
from enum import Enum
from dataclasses import dataclass

class HTTPContentType(Enum):
    HTML = 'text/html'
    JSON = 'application/json'
    PNG = 'image/png'

class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'
    PATCH = 'PATCH'

class HTTPStatusCode(Enum):
    OK = (200, 'OK')
    MOVED_PERMANENTLY = (301, 'Moved Permanently')
    NOT_FOUND = (404, 'Not Found')
    METHOD_NOT_ALLOWED = (405, 'Method Not Allowed')
    
@dataclass
class HTTPRequest:
    method: HTTPMethod
    url: str

DB = [
    {'id': 8, 'name': '전준우'},
    {'id': 34, 'name': '김원중'},
    {'id': 91, 'name': '윤동희'}
]

def get_user_from_db():
    return DB

# 요청을 분석하여 경로를 추출
def parseRequest(requests: str) -> HTTPRequest | None:
    if len(requests) < 1:
        return None
    
    arRequests = requests.split('\n') # 요청을 줄 단위로 분리
    for line in arRequests:
        match = re.search(r'\b(GET|POST|DELETE|PUT|PATCH)\b\s+(.*?)\s+HTTP/1.1', line)
        if match: # 위 패턴에 매치된다면
            req = HTTPRequest(HTTPMethod.GET, '')
            try:
                req.method = HTTPMethod(match.group(1))
                req.url = match.group(2)
            except:
                return None
            
            return req
            
    return None

# 응답 헤더 생성
def makeRespHeader(status: HTTPStatusCode, contentType: HTTPContentType, extra: dict|None = None) -> str:
    # resp = 'HTTP/1.1 200 OK\n'
    # resp += 'Content-Type: text/html\n'
    # resp += '\n
    
    resp = ''
    resp += f'HTTP/1.1 {status.value[0]} {status.value[1]}\n'
    resp += f'Content-Type: {contentType.value}\n'
    if extra is not None:
        for k, v in extra.items():
            resp += f'{k}: {v}\n'
    resp += '\n'
    return resp

def handle_request(req: HTTPRequest) -> bytes:
    arPath = ['/', '/users', '/lotte.png', '/giantsclub']

    if req is None:
        resp = makeRespHeader(HTTPStatusCode.METHOD_NOT_ALLOWED, HTTPContentType.HTML)
        
        # return해야 아래를 실행하지 않음
        return resp.encode('utf-8')

    # else
    strPath = req.url
    print(f'Path={strPath}')

    if strPath not in arPath:
        resp = makeRespHeader(HTTPStatusCode.NOT_FOUND, HTTPContentType.HTML)
        resp += '<html><body>404 Not Found</body></html>\n'

    elif strPath == '/users':
        resp = makeRespHeader(HTTPStatusCode.OK, HTTPContentType.JSON)
        users = get_user_from_db()
        resp += json.dumps(users)

    elif strPath == '/lotte.png':
        resp = makeRespHeader(HTTPStatusCode.OK, HTTPContentType.PNG)
        bResp = resp.encode('utf-8')

        with open('Day1\\lotte.png', 'rb') as f: # 바이너리 읽기
            bResp += f.read() # 메모리에 저장하므로 바이트 명시 X
        return bResp
    
    elif strPath == '/giantsclub':
        resp = makeRespHeader(HTTPStatusCode.MOVED_PERMANENTLY, HTTPContentType.HTML, {'Location': 'https://www.giantsclub.com'})

    else:
        resp = makeRespHeader(HTTPStatusCode.OK, HTTPContentType.HTML)
        resp += '<html><body>Hello World<img src = "/lotte.png"/></body></html>\n'
    
    return resp.encode('utf-8')


def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM) # IPv4, TCP
    try:
        # 전화번호 준비
        serverSocket.bind(('localhost', 8080))

        # 전화기 앞에서 대기
        serverSocket.listen()
    
        while True:
            # 전화가 오면 받기
            (cSocket, addr) = serverSocket.accept()
            print('Connection received from ', addr)

            # 고객 요청 듣기 (recv는 임의 처리)
            req = cSocket.recv(1024).decode('utf-8')
            print('req :', req)

            # 요청 처리
            httpReq = parseRequest(req)
            bResp = handle_request(httpReq)
            cSocket.sendall(bResp)

            # 전화 끊기
            cSocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print('\nShutting down the server.\n')
        serverSocket.close()

# 파일을 모듈로 활용할 때 필수
if __name__ == '__main__':
    createServer()

# 실행
# 웹브라우저 : 127.0.0.1:8080