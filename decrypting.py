
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://xn--wb0btwh7t3yibkc86i9tc5x9b.com/stegano.html')
driver.find_element_by_id("decode-file").send_keys(r'F:\2020JejuScienceHighSchool\과제연구\hidden.PNG')

driver.find_element_by_id("decode_btn").click()


print('finish')

#이게 우리가 스테가노 그래피로 얻은 결과
text="195 -114 -150 207 45 -72 179 -120 -110 191 39 -32 232 -15 -121 244 144 -43 11 -147 -113 23 12 -35 223 -66 -94 235 93 -16 118 -195 -250 130 -36 -172"
text=text.split(" ")

#제대로 split됬는지 확인
for i in range(0,len(text)):
    print(text[i])

x1,y1,z1= 15,195,250
x2,y2,z2= 3,36,172
msg=''

for i in range(0,len(text),6):
    a1=int(text[i+0])
    b1=int(text[i+1])
    c1=int(text[i+2])
    a2=int(text[i+3])
    b2=int(text[i+4])
    c2=int(text[i+5])

    k=((a2*y1)-(a2*y2)+b2*(x2-x1))/((a1*b2)-(a2*b1))
    k=int(k)

    r=a1*k+x1
    r="{0:x}".format(r)
    g=b1*k+y1
    g="{0:x}".format(g)
    b=c1*k+z1
    b="{0:x}".format(b)
    print(str(r)+' '+str(g)+' '+str(b))
    msg=msg+str(r)+' '+str(g)+' '+str(b)+' '


print('apple')
msg=msg[0:len(msg)-1]
print(msg)
print('finish')

final_msg=''
msg=msg.split(' ')
msg=msg[0:len(msg)-2]
for i in range(0,len(msg)):
    final_msg=final_msg+msg[i]+' '

final_msg=final_msg[0:len(final_msg)-1]
print(final_msg)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://aes.online-domain-tools.com/')

intxt = final_msg

object = driver.find_element_by_id("frm-text")
object.send_keys(intxt)

key="0fc3fa0324ac"
elem = driver.find_element_by_id("frmform-key")
elem.send_keys(key)

driver.find_element_by_id("frm-text_type-hex").click()
driver.find_element_by_id("frm-form-decrypt").click()
