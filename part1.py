from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://xn--wb0btwh7t3yibkc86i9tc5x9b.com/stegano.html')
driver.find_element_by_css_selector("input[type='file']").send_keys(r'F:\2020JejuScienceHighSchool\과제연구\test.JPG')
#driver.find_element_by_class_name('form-control message').send_keys('Hello World!')
driver.find_element_by_class_name('encode btn btn-default pull-right').click()
print('finish')
