import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1374240204@qq.com'
password = ''
receivers = ['w@wktadmin.com', '1374240204@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
smtp_server = 'smtp.qq.com'
smtp_port = 25

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('你真牛皮', 'plain', 'utf-8')
message['From'] = Header("wang", 'utf-8')  # 发送者
message['To'] = Header("wang", 'utf-8')  # 接收者

subject = '不要脸'
message['Subject'] = Header(subject, 'utf-8')
smtpObj = smtplib.SMTP(smtp_server, smtp_port)
smtpObj.login(sender, password)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")
