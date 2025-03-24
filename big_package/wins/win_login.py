# 公共库
import tkinter as tk
import os
# 项目库
from ..pub_fun import fun_win
from ..client_net import uno_client


class login_win:
    def __init__(self):
        # 需要传递的参数
        self.username = ''
        self.car_code = 0
        # 中途变量

        # 属性定义
        self.win = tk.Tk()
        fun_win.center_window(self.win, 800, 600)
        # 登录窗口布局
        # 退出按钮
        self.bu_exit = tk.Button(self.win, bg='#cf7676', font=('Times', 30), text="退出", command=fun_win.exit_tip)
        self.bu_exit.place(x=0, y=0, width=100, height=60)
        # 设置按钮
        self.bu_set = tk.Button(self.win, bg='#cf7676', font=('Times', 30), text="设置", command=fun_win.exit_tip)
        self.bu_set.place(x=700, y=0, width=100, height=60)
        # 选角色背景
        self.la_select_car = tk.Label(self.win, bg='#a8bee6', font=('Times', 25), text="请选择头像", anchor='n', pady=20)
        self.la_select_car.place(x=50, y=120, width=700, height=250)
        # 角色头像
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        self.photo_1 = fun_win.open_img(
            os.path.join(current_file_path, '..', '..', '..', 'UNO_Assets', 'Avatars', 'dog_hat.png'), 100, 100)
        self.photo_2 = fun_win.open_img(
            os.path.join(current_file_path, '..', '..', '..', 'UNO_Assets', 'Avatars', 'dog_black.png'), 100, 100)
        self.photo_3 = fun_win.open_img(
            os.path.join(current_file_path, '..', '..', '..', 'UNO_Assets', 'Avatars', 'dog_yellow.png'), 100, 100)
        self.photo_4 = fun_win.open_img(
            os.path.join(current_file_path, '..', '..', '..', 'UNO_Assets', 'Avatars', 'orange.png'), 100, 100)
        self.la_ava_1 = tk.Label(self.win, image=self.photo_1)
        self.la_ava_2 = tk.Label(self.win, image=self.photo_2)
        self.la_ava_3 = tk.Label(self.win, image=self.photo_3)
        self.la_ava_4 = tk.Label(self.win, image=self.photo_4)
        self.la_ava_1.img = self.photo_1
        self.la_ava_2.img = self.photo_2
        self.la_ava_3.img = self.photo_3
        self.la_ava_4.img = self.photo_4
        self.la_ava_1.place(x=100, y=200)
        self.la_ava_2.place(x=269, y=200)
        self.la_ava_3.place(x=434, y=200)
        self.la_ava_4.place(x=600, y=200)
        self.bu_sel_1 = tk.Button(self.win, bg='#e3819d', font=('Times', 14), text="未选择",
                                  command=lambda: self.change_code(1, self.bu_sel_1, self.bu_sel_2, self.bu_sel_3,
                                                                   self.bu_sel_4))
        self.bu_sel_1.place(x=100, y=310, width=100, height=30)
        self.bu_sel_2 = tk.Button(self.win, bg='#e3819d', font=('Times', 14), text="未选择",
                                  command=lambda: self.change_code(2, self.bu_sel_2, self.bu_sel_1, self.bu_sel_3,
                                                                   self.bu_sel_4))
        self.bu_sel_2.place(x=269, y=310, width=100, height=30)
        self.bu_sel_3 = tk.Button(self.win, bg='#e3819d', font=('Times', 14), text="未选择",
                                  command=lambda: self.change_code(3, self.bu_sel_3, self.bu_sel_1, self.bu_sel_2,
                                                                   self.bu_sel_4))
        self.bu_sel_3.place(x=434, y=310, width=100, height=30)
        self.bu_sel_4 = tk.Button(self.win, bg='#e3819d', font=('Times', 14), text="未选择",
                                  command=lambda: self.change_code(4, self.bu_sel_4, self.bu_sel_1, self.bu_sel_2,
                                                                   self.bu_sel_3))
        self.bu_sel_4.place(x=600, y=310, width=100, height=30)
        self.en_username = tk.Entry(self.win, justify='center', bg="#e5e5e5", font=("Times", 18))
        self.en_username.place(x=250, y=390, width=300, height=60)
        self.en_username.insert(tk.END, '请输入昵称')  # 插入提示文本
        self.en_username.config(fg='grey')  # 设置文本颜色为灰色
        self.en_username.bind('<FocusIn>', self.on_entry_click)  # 绑定点击事件
        self.bu_login = tk.Button(self.win, bg='#e89954', font=("Times", 35), text="登录",
                                  command=self.connect_server_check)
        self.bu_login.bind('<Enter>', self.on_enter)
        self.bu_login.bind('<Leave>', self.on_leave)
        self.bu_login.place(x=300, y=465, width=200, height=100)

    # 选角按钮
    def change_code(self, n, bu_g, bu_r1, bu_r2, bu_r3):
        self.car_code = n
        # 变颜色与文本
        bu_g.config(bg='#73c493', text="已选择")
        bu_r1.config(bg='#e3819d', text="未选择")
        bu_r2.config(bg='#e3819d', text="未选择")
        bu_r3.config(bg='#e3819d', text="未选择")

    # 输入昵称
    def on_entry_click(self, event):
        if self.en_username.get() == '请输入昵称':
            self.en_username.delete(0, tk.END)  # 删除提示文本
            self.en_username.config(fg='black')  # 设置文本颜色为黑色

    # 登录按钮
    def connect_server_check(self):
        # 登录时先获取用户昵称
        self.username = self.en_username.get()

        # 向服务器发送A类数据
        A_manager = uno_client.client_nuo()
        A_manager.A_data_fun(self.username, self.car_code)
        can_ready = A_manager.can_ready
        print(can_ready)

        # 检查can_ready
        if can_ready == 1:
            print("can ready!")
            self.win.destroy()
        else:
            print("can't ready!")

    def on_enter(self, event):
        self.bu_login.config(bg='#87F5AB')  # 鼠标悬停时变为绿色

    def on_leave(self, event):
        self.bu_login.config(bg='#e89954')  # 鼠标离开时回复默认颜色

    # 运行窗口
    def run(self):
        self.win.mainloop()
