#! /usr/bin/python
#! coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage


mail_host="smtp.qq.com"
mail_user="wpl@imobpay.com"
mail_pass="fight19900307"

sender = 'wpl@imobpay.com'
receivers = ['364508527@qq.com', '2980566214@qq.com']


message = MIMEMultipart('related')
message['From'] = Header("王朋亮", 'utf-8')
message['to'] = Header("My QQ", 'utf-8')

subject = 'Python SMTP MailTest'
message['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)


mail_msg="""
<p> Python 发送邮件测试...</p>
<p><a href="http://map.baidu.com/?newmap=1&s=s%26wd%3D%E9%83%91%E5%B7%9E%E5%B8%82%26c%3D268&from=alamap&tpl=mapcity">郑州地图</a></p>
<p>图片演示:</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8')) 

fp = open('link.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("MailSend Success!")
except smtplib.SMTPException as Argument:
    print ("MailSend Error: ", Argument)
