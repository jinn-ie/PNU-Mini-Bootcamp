from socket import *

def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)
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

            # 고객에게 응답하기
            res = 'HTTP/1.1 200 OK\n'
            res += 'Content-Type: text/html\n'
            res += '\n' # header와 body 사이 줄바꿈
            res += '<html><body>Hello World</body></html>\n'
            cSocket.sendall(res.encode('utf-8'))

            # 전화 끊기
            cSocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print('\nShutting down the server.\n')
        serverSocket.close()

# 파일을 모듈로 활용할 때 필수
if __name__ == '__main__':
    createServer()

# 실행
# 터미널 : python day1_http서버구현.py
# 웹브라우저 : 127.0.0.1:8080