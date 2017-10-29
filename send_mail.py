#!/usr/bin/python
# -*- coding:utf8 -*-
# Author:ZLF

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('邮件内容','plain','utf-8')
msg['From']=formataddr(['zlf','13314093559@163.com'])
msg['To']=formataddr(['myself','18637993678@wo.cn'])
msg['Subject']='主题'

server = smtplib.SMTP('smtp.163.com',25)
server.login('13314093559@163.com','1neversaygoodbye')
server.sendmail('13314093559@163.com',['18637993678@wo.cn',],msg.as_string())
server.quit()