# -*- coding:utf-8 -*-
# Author: yanghuyuan
# Date: 2018/9/10

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("今天很开心", "html", "utf-8")
msg["From"] = "idocker@qq.com"
msg["To"] = "mail@qq.com"
msg["Subject"] = "今天很开心"

server = smtplib.SMTP()
server.connect("smtp.qq.com", 25)
server.login("idocker@qq.com", "hqnwtockufkgdcac")
server.sendmail("idocker@qq.com", "mail@qq.com", msg.as_string())
server.quit()
