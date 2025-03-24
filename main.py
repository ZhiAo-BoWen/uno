# 公共库

# 项目库
from big_package.wins import win_login, win_ready

# 公有变量

if __name__ == '__main__':
    # pyinstaller封装命令
    # pyinstaller --add-data 'UNO_Assets/Avatars;UNO_Assets/Avatars' .\main.py
    # 启动登录页
    win_login_ = win_login.login_win()
    win_login_.run()

    # 启动准备页
    # win_ready_ = win_ready.ready_win()
    # win_ready_.run()
