# 导入公共库
import json
import socket
# 导入项目库

server_sock_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock_.bind(("127.0.0.1", 8888))
try:
    while True:
        # 接受所有数据
        client_data, client_player = server_sock_.recvfrom(1024)
        client_data = json.loads(client_data.decode('utf-8'))
        print(client_data, client_player)

        # 数据分类
        match client_data["msg_type"]:
            case "A":
                # 加入数据来源
                print("是A类数据！")
                client_data["client_player"] = str(client_player[0])
                A_data = client_data
                print(A_data)

                # 回应客户端
                A_data_ = {"players_info": [], "can_ready": 1}
                # 序列化字典
                A_data_ = json.dumps(A_data_).encode('utf-8')
                server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                server_sock.sendto(A_data_, (A_data["client_player"], 6666))
                server_sock.close()
            case "B":
                print("是B类数据！")
finally:
    server_sock_.close()

