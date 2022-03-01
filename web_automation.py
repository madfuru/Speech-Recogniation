import smtplib
mail = 'mjmadjan010@gmail.com'
password = 'mjaadnaanni%1<0=10'
d = 'madhanmady010@gmail.com'
def sendmail():
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(mail,password)
        server.sendmail(d,'hello')
        server.close()
        print('mail has sent')
