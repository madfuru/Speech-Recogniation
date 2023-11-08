from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import pyttsx3 as p

class info():
    def __init__(self):
        self.s = Service("C:\developer/chromedriver.exe")
        self.deriver = webdriver.Chrome(service=self.s)

    def get_info(self,query):
        self.query = query
        self.deriver.get(url='https://www.wikipedia.org/')
        search = self.deriver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        search_button = self.deriver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        search_button.click()

        info = self.deriver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[3]/li[2]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()
        print(readable_text)

        self.deriver.quit()

#bot = info()
#bot.get_info()
