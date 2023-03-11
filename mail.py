# -- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email import charset

#各種情報
#account
#password
#server
#from_addr
#to_addr



#SMTPサーバーに接続する
con = smtplib.SMTP(server, 587)
con.set_debuglevel(1)
con.starttls()
con.login(account, password)

#送信するメールのメッセージを作成する
cset = 'utf-8'
message = MIMEText(u'SMTPのテスト', 'plain', cset)
message['Subject'] = Header(u'SMTP経由での電子メール送信のテストです', cset)
message['From'] = from_addr
message['To'] = to_addr

#メールを送信する
con.sendmail(from_addr, [to_addr], message.as_string())

#SMTPから切断する
con.close()