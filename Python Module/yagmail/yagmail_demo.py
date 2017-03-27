import yagmail
yag = yagmail.SMTP(user='zhenxing1004@hotmail.com', password='xxxx', host='smtp-mail.outlook.com', port='587')
body = "附件为Python学习资料，请查收"
yag.send(to='980692043@qq.com', subject='Python学习资料', contents=[body,'/home/zhenxing/Python.png'])
print("已发送邮件")