# 公共库
import tkinter as tk
# 项目库
from ..pub_fun.fun_win import center_window


class ready_win:
    def __init__(self):
        # 需要的参数

        # 定义一个窗口
        self.win = tk.Tk()
        center_window(self.win, 800, 600)  # 引用fun_win中的函数创建一个窗口
        # 准备玩家头像背景
        self.la_player_bg1 = tk.Label(self.win, bg='#808080')
        self.la_player_bg1.place(x=100, y=200, width=100, height=100)
        self.la_player_bg2 = tk.Label(self.win, bg='#808080')
        self.la_player_bg2.place(x=266, y=200, width=100, height=100)
        self.la_player_bg3 = tk.Label(self.win, bg='#808080')
        self.la_player_bg3.place(x=436, y=200, width=100, height=100)
        self.la_player_bg4 = tk.Label(self.win, bg='#808080')
        self.la_player_bg4.place(x=600, y=200, width=100, height=100)
        # 显示玩家名字
        self.la_player_name1 = tk.Label(self.win, bg='#9be8e7', font=('Times', 20), text='asdfa')
        self.la_player_name1.place(relx=0.5, anchor='center')
        # self.la_player_name1 = tk.Label(self.win, bg='#9be8e7', font=('Times', 20), text='asdfa')
        # self.la_player_name1.place(x=113, y=150)
        # self.la_player_name1 = tk.Label(self.win, bg='#9be8e7', font=('Times', 20), text='asdfa')
        # self.la_player_name1.place(x=113, y=150)
        # self.la_player_name1 = tk.Label(self.win, bg='#9be8e7', font=('Times', 20), text='asdfa')
        # self.la_player_name1.place(x=113, y=150)

    def run(self):
        self.win.mainloop()
