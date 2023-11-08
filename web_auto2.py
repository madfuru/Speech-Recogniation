import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from pywinauto import application
import smtplib
mail = 'mjmadjan010@gmail.com'
password = 'mjaadnaanni%1<0=10'

class Music():
    def __init__(self):
        self.s = Service("C:\developer/chromedriver.exe")
        self.deriver = webdriver.Chrome(service=self.s)

    def play(self,name):
        self.name = name
        self.deriver.get(url='https://www.youtube.com/'+name)
        video = self.deriver.find_element_by_xpath('//*[@id="hover-overlays"]')
        video.click()

    def notepad(self,name):
        self.name = name
        app = application.Application()
        app.start('C:\\WINDOWS\\system32\\notepad.exe')
        write = app.top_window_()
        write.TypeKeys(name)

    def sendmail(self,to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(mail,password)
        server.sendmail(mail,to+'@gmail',content)
        server.close()
#bot = Music()
#bot.play('arabic kuthu')