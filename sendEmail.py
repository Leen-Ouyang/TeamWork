import smtplib
from email.mime.text import MIMEText #设置邮件正文
from email.header import Header #设置邮件头

# 登陆smtp服务器
mail_obj = smtplib.SMTP("smtp.qq.com", 25) #设置服务器 端口号
mail_obj.login("1283117490@qq.com", "xizzgvtqcuoefhcc") # 发送邮件的邮箱地址和授权码

# 设置发送邮箱和收件邮箱 此处可不定义 直接写入mail_obj.sendmail()
mail_user = "1283117490@qq.com"
mail_receivers = "ganyu_hutao@163.com"	# 收件人可以设置多个

# 邮件内容
mail_msg = MIMEText("经验+3", "plain", "utf-8")  # 邮件文本  类型  编码
mail_msg["From"] = "jy3<1283117490@qq.com>"  #  发件人  编码
mail_msg["To"] = "ganyu_hutao@163.com"  # 收件人 编码
mail_msg["Subject"] = Header("666", "utf-8") # 主题 编码

# 发送邮件
mail_obj.sendmail(mail_user, mail_receivers, mail_msg.as_string())
