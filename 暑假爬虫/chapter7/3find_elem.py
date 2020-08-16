from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# 1
input_first = browser.find_element_by_id('q')
# 2
input_second = browser.find_element_by_css_selector('#q')
# 3
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
