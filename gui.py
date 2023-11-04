from GlobalSetting import excelfile, sender_email, sender_password #导入全局变量
import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import Style
from tkinter import ttk
from tkinter import messagebox

# 创建GUI界面
root = tk.Tk()
root.geometry("600x400")
root.title("成绩单发送程序")

style = Style(theme='litera')  # 使用litera主题

# 用于获取文件路径
excelfile = ''

# 获取文件路径
def get_file_path():
    global excelfile
    excelfile = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
    status_label.config(text="文件路径已选择：" + excelfile)
    file_entry.delete(0, tk.END)  # 清空文本框
    file_entry.insert(0, excelfile)  # 填充文件路径

# 用于提交操作
def submit(excelfile, sender_email, sender_password):
    try:
        status_label.config(text="")  # 清空错误消息
        if not excelfile:
            raise Exception("101 未提交文件！")
        if not sender_email:
            raise Exception("102 未输入用户名！")
        if not sender_password:
            raise Exception("103 未输入密码！")
        if not excelfile.endswith('.xlsx'):
            raise Exception("104 文件格式错误！")
        # 在这里编写你的逻辑代码
        print("文件路径: ", excelfile)
        print("邮箱账户: ", sender_email)
        print("邮箱密码: ", sender_password)
    except Exception as e:
        messagebox.showerror("错误", str(e))

# 错误提示
def show_error_info():
    # 创建新的窗口
    new_window = tk.Toplevel()
    new_window.title("错误提示")

    # 在新窗口中显示返回的值
    error_label = tk.Label(new_window, text="Error Value: " + str(error_value))
    error_label.pack(padx=20, pady=20)

    # 运行新窗口的事件循环
    new_window.mainloop()



# 创建界面元素
file_frame = ttk.Frame(root)
file_frame.pack(padx=10, pady=10, fill='x')

file_label = ttk.Label(file_frame, text="文件查询:")
file_label.pack(side="left", padx=5, pady=5)

file_entry = ttk.Entry(file_frame, width=40)
file_entry.pack(side="left", padx=5, pady=5)

file_button = ttk.Button(file_frame, text="选择文件", command=get_file_path)
file_button.pack(side="left", padx=5, pady=5)

user_frame = ttk.Frame(root)
user_frame.pack(padx=10, pady=10, fill='x')

user_label = ttk.Label(user_frame, text="邮箱账户:")
user_label.pack(side="left", padx=5, pady=5)

user_entry = ttk.Entry(user_frame, width=30)
user_entry.pack(side="left", padx=5, pady=5)

password_frame = ttk.Frame(root)
password_frame.pack(padx=10, pady=10, fill='x')

password_label = ttk.Label(password_frame, text="邮箱密码:")
password_label.pack(side="left", padx=5, pady=5)

password_entry = ttk.Entry(password_frame, show="*", width=30)
password_entry.pack(side="left", padx=5, pady=5)

# 提交函数
def on_submit():
    excelfile = file_entry.get()
    sender_email = user_entry.get()
    sender_password = password_entry.get()
    submit(excelfile, sender_email, sender_password)

submit_button = ttk.Button(root, text="提交", command=on_submit, width=20)
submit_button.pack(padx=10, pady=10, fill='x')

status_label = ttk.Label(root, text="")
status_label.pack(padx=10, pady=10, fill='x')

root.mainloop()

##################

error_value = 101  # 假设这是从另一个程序返回的值
show_error_info(error_value)
