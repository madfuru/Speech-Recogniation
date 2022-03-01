from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class Movie():
    def __init__(self):
        self.s = Service("C:\developer/chromedriver.exe")
        self.deriver = webdriver.Chrome(service=self.s)

    def movie_review(self,name):
        self.deriver.get(url="https://www.google.com/")
        search = self.deriver.find_element_by_css_selector("form input")
        search.click()
        search.send_keys(name + " movie review")
        search.send_keys(Keys.ENTER)
#bot = Movie()
#bot.movie_review('Extraction')