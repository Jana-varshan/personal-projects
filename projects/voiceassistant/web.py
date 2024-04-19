from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class infow():
    # def __init__(self):




    def google(self,query):
        self.driver = webdriver.Chrome()
        self.driver.get(url='https://www.google.com')
        search=self.driver.find_element(by="name",value="q")
        search.click()
        search.send_keys(query)
        search.send_keys(Keys.ENTER)


