import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))

strCmd = '''GET / HTTP/1.1
Host: localhost:8080

'''.encode()
s.send(strCmd)
while True:
    resp = s.recv(1024)
    if not resp or len(resp) < 1:
        break
    print(resp.decode(), end='')
s.close()

# 터미널에서 실행
# 서버 -> 클라이언트
# python http클라이언트구현.py