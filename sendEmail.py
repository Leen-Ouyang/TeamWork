import smtplib                          # smtplib模块
import json                             # 处理json
import GlobalSetting                    # 全局变量
from email.mime.text import MIMEText    # 纯文本，HTML
from email.mime.image import Header     # 处理邮件头

# 发送邮件
def sendEmail(sender_email, sender_password):

    # 登陆smtp服务器
    mail_obj = smtplib.SMTP("smtp.qq.com",25)       # 设置服务器 端口号
    mail_obj.login(sender_email, sender_password)   # 发送邮件的邮箱地址和授权码

    # 设置发送邮箱和收件邮箱 此处可不定义 直接写入mail_obj.sendmail()
    mail_user = sender_email

    '''

    mail_receivers = ["收件箱1","收件箱2","收件3"]   # json提取
    getJsonData("email.json")["receivers"]          # json提取

    # 处理json文件
    for i in length(mail_receivers):

            # 邮件内容
            mail_msg =MIMEText("邮件文本","plain","utf-8")  # 邮件文本  类型  编码
            mail_msg["From"] = Header("设置发件人","utf-8") # 发件人  编码
            mail_msg["To"] = Header("设置收件人","utf-8")   # 收件人 编码
            mail_msg["Subject"] = Header("设置主题","utf-8")# 主题 编码

            # 发送邮件
            mail_obj.sendamil(mail_user, mail_receivers, mail_msg.as_string())

    '''

def main():
    sendEmail("发送邮箱","授权码")

