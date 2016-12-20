#! /usr/bin/python
#! coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


mail_host="smtp.qq.com"
mail_user="wpl@imobpay.com"
mail_pass="fight19900307"

sender = 'wpl@imobpay.com'
receivers = ['364508527@qq.com', '2980566214@qq.com']

mail_msg="""
<p> Python 发送邮件测试...</p>
<p><a href="http://www.runoob.com">www.runoob.com</a></p>
"""


message = MIMEMultipart()
message['From'] = Header("王朋亮", 'utf-8')
message['to'] = Header("My QQ", 'utf-8')

subject = 'Python SMTP MailTest'
message['Subject'] = Header(subject, 'utf-8')


#part = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')    #发送简单测试邮件
part = MIMEText(mail_msg, 'html', 'utf-8')    #发送Html格式内容邮件  
message.attach(part)

#加附件
part = MIMEApplication(open('foo.txt','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="foo.txt")
message.attach(part)



try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("MailSend Success!")
except smtplib.SMTPException as Argument:
    print ("MailSend Error: ", Argument)
