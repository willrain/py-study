import smtplib

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#print(smtp)

# 서버 연결 확인
print(smtp.ehlo())

# 서버 로그인
smtp.login('willrain75@gmail.com', 'Tmdghks01!')


# 접속종료
smtp.quite()
