import socket
import json

# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到端口
server_address = ('localhost', 10000)
sock.bind(server_address)

try:
    while True:
        print('Waiting to receive message')
        data, address = sock.recvfrom(4096)

        print(f'Received {len(data)} bytes from {address}')
        data_json = data.decode('utf-8')
        data_dict = json.loads(data_json)
        print(f'Received message: {data_dict}')
finally:
    # 关闭套接字
    sock.close()
