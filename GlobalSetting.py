# 模块导入
import os

#邮件设置
##收件地址设置
receive_address = "abc051@163.com"
##发送账户设置
sender_email = "1283117490@qq.com"
sender_password = "xizzgvtqcuoefhcc"

# 文件路径
##执行目录
current_directory = os.path.dirname(os.path.abspath(__file__))
##输入文件路径
excelfile = os.path.join(current_directory, "excel","成绩表.xlsx")
##过程json文件路径
jsonfile = os.path.join(current_directory, "temp.json")