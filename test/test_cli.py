import socket
import json

# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 要发送的字典
data_dict = {'key1': 'value1', 'key2': 123}

# 序列化字典为JSON字符串
data_json = json.dumps(data_dict)

# 编码JSON字符串为字节
data_bytes = data_json.encode('utf-8')

# 目标地址和端口
server_address = ('localhost', 10000)

try:
    # 发送数据
    sent = sock.sendto(data_bytes, server_address)
    print(f'Sent {sent} bytes to {server_address}')
finally:
    # 关闭套接字
    sock.close()
