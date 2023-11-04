import GlobalSetting #导入全局变量
import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 创建GUI界面
root = tk.Tk()
root.geometry("600x400")
root.title("成绩单发送程序")

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
        status_label.config(text="")  # 清空前一次的状态消息
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
        status_label.config(text="错误：{}".format(e))

# 创建界面元素
file_label = tk.Label(root, text="文件查询:")
file_label.pack()

file_entry = tk.Entry(root, width=60)
file_entry.pack()

file_button = tk.Button(root, text="选择文件", command=get_file_path)
file_button.pack()

user_label = tk.Label(root, text="邮箱账户:")
user_label.pack()

user_entry = tk.Entry(root, width=30)
user_entry.pack()

password_label = tk.Label(root, text="邮箱密码:")
password_label.pack()

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

# 提交函数
def on_submit():
    excelfile = file_entry.get()
    sender_email = user_entry.get()
    sender_password = password_entry.get()
    submit(excelfile, sender_email, sender_password)

submit_button = tk.Button(root, text="提交", command=on_submit)
submit_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()