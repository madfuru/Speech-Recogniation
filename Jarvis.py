from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pywinauto import application
import pyttsx3 as p

class offine_music():
    def __init__(self):
        self.s = Service("C:\developer/chromedriver.exe")
        self.deriver = webdriver.Chrome(service=self.s)

    def desktop_music(self,name):

       offine= self.deriver.get('C:\\Users\\@madan\\Music\\'+name)
        #offine = self.deriver.find_element_by_xpath('//*[@id="tbody"]/tr[16]/td[1]/a')

#bot = offine_music()
#bot.music('Otilia-Bilionera.mp3')

