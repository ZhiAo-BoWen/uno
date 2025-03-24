# 公共库
import socket
import json
import threading

# 项目库


class client_nuo:
    def __init__(self):
        # 汇总要向服务器返回的数据（dict）
        self.A_data = {}
        self.B_data = {}
        self.C_data = {}
        self.D_data = {}
        self.can_ready = 0
        self.server_info = ('127.0.0.1', 8888)

    def A_data_fun(self, username, car_code):
        # 创建socket
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # 序列化字典
            self.A_data = {"msg_type": "A", 'username': username, 'select_code': car_code}
            self.A_data = json.dumps(self.A_data).encode('utf-8')
            # 发送
            client_sock.sendto(self.A_data, self.server_info)
            print(self.A_data)
        finally:
            client_sock.close()

        client_sock_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_sock_.bind(("127.0.0.1", 6666))
        try:
            while True:
                # 接受所有数据
                server_data = client_sock_.recvfrom(1024)[0]
                server_data = json.loads(server_data.decode('utf-8'))
                print(server_data, type(server_data))
                if server_data["can_ready"] == 1:
                    self.can_ready = 1
                    print("可以准备了")
                    client_sock.close()
                    break
                else:
                    print("不能准备")
                    client_sock.close()
                    break
        finally:
            client_sock_.close()

