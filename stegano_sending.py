from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://xn--wb0btwh7t3yibkc86i9tc5x9b.com/stegano.html')
driver.find_element_by_css_selector("input[type='file']").send_keys(r'F:\2020JejuScienceHighSchool\과제연구\test.JPG')

msg="1 0 23 423 534 123 123 1234 234 21"
object = driver.find_element_by_id("input_message")
object.send_keys(msg)
btn = driver.find_element_by_id("encode_btn")
btn.click()


print('finish')
