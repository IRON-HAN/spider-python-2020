from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from taobao import settings


class taobao:
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url
        self.browser = webdriver.Firefox(executable_path = r'E:\1_JB\Python\暑假爬虫\taobao\geckodriver.exe')
        self.wait = WebDriverWait(self.browser, 10)

    def login(self):
        self.browser.get(self.url)
        # if self.browser.find_element_by_xpath('//*[@id="fm-login-id"]'):
        #     user=self.browser.find_element_by_xpath('//*[@id="fm-login-id"]')
        #     user.send_keys(settings.USER)
        # if self.browser.find_element_by_xpath('//*[@id="fm-login-password"]'):
        #     user=self.browser.find_element_by_xpath('//*[@id="fm-login-password"]')
        #     user.send_keys(settings.PASSWORD)
        if self.browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div/div[1]/i'):
            saoma=self.browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div/div[1]/i')
            saoma.click()
        # commit=self.browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/div/form/div[4]/button')
        # commit.click()



if __name__ == '__main__':
    taobao().login()
