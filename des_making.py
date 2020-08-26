from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://des.online-domain-tools.com/')

intxt = "맨유 트레블"
object = driver.find_element_by_id("frm-text")
object.send_keys(intxt)
key = '1234'
elem = driver.find_element_by_id("frmform-key")
elem.send_keys(key)
select = Select(driver.find_element_by_id("frmform-function"))
select.select_by_value("aes")
driver.find_element_by_id("frm-form-encrypt").click()
