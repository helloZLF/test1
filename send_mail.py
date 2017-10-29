#!/usr/bin/python
# -*- coding:utf8 -*-
# Author:ZLF

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('邮件内容','plain','utf-8')
msg['From']=formataddr(['zlf','发件箱])
msg['To']=formataddr(['myself','收件箱])
msg['Subject']='主题'

server = smtplib.SMTP('smtp.163.com',25)
server.login('发件箱账号','发件箱密码')
server.sendmail('发件箱',['收件箱',],msg.as_string())
server.quit()