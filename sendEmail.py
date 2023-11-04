import smtplib
from email.mime.text import MIMEText #设置邮件正文
from email.header import Header #设置邮件头
from GlobalSetting import receive_address
from text import generate_report,number_of_students
from gui import sender_email, sender_password

def sendEmail():
    # 登陆smtp服务器
    mail_obj = smtplib.SMTP("smtp.qq.com", 25) #设置服务器 端口号
    mail_obj.login(sender_email, sender_password) # 发送邮件的邮箱地址和授权码
    #mail_obj.login("1283117490@qq.com", "xizzgvtqcuoefhcc") # 发送邮件的邮箱地址和授权码

    # 设置发送邮箱和收件邮箱 此处可不定义 直接写入mail_obj.sendmail()
    mail_user = "1283117490@qq.com"
    mail_receivers = receive_address	# 收件人可以设置多个

    print(number_of_students)

    # 发送邮件
    for count in range(number_of_students):
        # 邮件内容
        print("开始发送第{count}条")
        mail_msg = MIMEText(generate_report(count), "plain", "utf-8")  # 邮件文本  类型  编码
        mail_msg["From"] = "jy3<1283117490@qq.com>"  #  发件人  编码
        mail_msg["To"] = receive_address  # 收件人 编码
        mail_msg["Subject"] = Header("教务处成绩通知", "utf-8") # 主题 编码
        #发送
        mail_obj.sendmail(mail_user, mail_receivers, mail_msg.as_string())
        print("第{count}条发送完毕")
