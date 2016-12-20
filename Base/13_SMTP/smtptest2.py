#! /usr/bin/python

import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication  

_user = "wpl@imobpay.com"  
_pwd  = "fight19900307"  
_to   = "364508527@qq.com"  


msg = MIMEMultipart()  
msg["Subject"] = "Python Mail Test"  
msg["From"]    = _user  
msg["To"]      = _to  

#---这是文字部分---  
part = MIMEText("乔装打扮，不择手段")  
msg.attach(part)  

#---这是附件部分---  
#pdf类型附件  
part = MIMEApplication(open('foo.pdf','rb').read())  
part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")  
msg.attach(part)  


s = smtplib.SMTP("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25  
s.login(_user, _pwd)#登陆服务器  
s.sendmail(_user, _to, msg.as_string())#发送邮件  
s.close()  
