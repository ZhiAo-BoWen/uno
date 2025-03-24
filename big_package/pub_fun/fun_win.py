from PIL import ImageTk, Image


# 窗口初始化
def center_window(win, width, height):
    # 设置标题
    win.title("UNO!")
    # 设置背景色
    win.config(bg='#9be8e7')
    # 置于顶层
    win.attributes('-topmost', True)
    # 锁定窗口缩放
    win.resizable(False, False)
    # 窗口居中
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    win.geometry('%dx%d+%d+%d' % (width, height, x, y))


# 打开图片变为label使用的img类型
def open_img(img_path, width, height):
    # 打开图片文件
    image = Image.open(img_path)
    # 调整图片大小以匹配窗口大小
    image = image.resize((width, height))
    # 将PIL图片转换为Tkinter可用的格式
    photo = ImageTk.PhotoImage(image)
    return photo


# 退出提示
def exit_tip():
    pass
