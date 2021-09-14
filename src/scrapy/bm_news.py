from selenium import webdriver
import time

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com/search?q=banco+inter&tbs=qdr:d,sbd:1&tbm=nws&source=lnt&sa=X&ved=0ahUKEwj_rrjejonmAhVaHrkGHcwtBWAQpwUIHw&biw=1045&bih=745&dpr=1'
        self.search_bar = 'q'  # tipo usado ( name )

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):              # barra de pesquisa
        self.driver.find_element_by_xpath(xpath)
        time.sleep(1)


goo = webdriver.Chrome("../../resources/chromedriver.exe")    # local do browser driver
g = Google(goo)
g.navigate()
xpath = "//*[@id=\"rso\"]/div/div[1]/div/div/h3"
este = goo.find_element_by_xpath(xpath)
print(este)

time.sleep(5)
goo.quit()