from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path = './chromedriver')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id("switcher_plogin")
a_tag.click()

user_tag = bro.find_element_by_id('u')
pass_tag = bro.find_element_by_id('p')
sleep(1)
user_tag.send_keys('2674467254')
sleep(1)
pass_tag.send_keys('.2674467254')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()
sleep(2)
bro.quit()
