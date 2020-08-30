#===================================================================================================
#이미지 불러와서 사이즈 리사이징
#===================================================================================================
from PIL import Image
import numpy as np
import math

img_name='test.jpg'
im=Image.open(img_name)

width, height=im.size
ratio = width / height
re_height=100
re_width = round(ratio*re_height)
re_im = im.resize((re_width, re_height))

pix = np.array(re_im)
print(re_im.size)

'''
f=open('img_information.txt','w')
for i in range(0,re_height,1):
      for j in range(0,re_width,1):
            r,g,b=pix[i][j]
            f.write('x좌표 : '+str(i)+' y좌표 : '+str(j)+' -> '+str(r)+','+str(g)+','+str(b)+','+'\n')
f.close()
'''

#===================================================================================================
#웹 크롤링을 이용해서 문장 des암호화
#===================================================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://aes.online-domain-tools.com/')

#key = input("키를 입력하세요 : ")
intxt = "맨유 트레블"

object = driver.find_element_by_id("frm-text")
object.send_keys(intxt)

#임시 key설정
key="0f3b7c"
elem = driver.find_element_by_id("frmform-key")
elem.send_keys(key)

#여기 부분 아직 안됨 ㅅㅂ
"""
driver.find_element_by_id("frmform-function").click()
select = Select(driver.find_element_by_id("frmform-function"))
select.select_by_value("aes")

#driver.find_element_by_css_selector("input[type='radio'][value='hex']")
"""

driver.find_element_by_id("frm-form-encrypt").click()

#===================================================================================================
#des 암호화 결과 rgb로 처리
#===================================================================================================
#===================================================================================================
#rgb처리 결과 암호화
#===================================================================================================
from random import *

msg=''
hexcode="f7	f9	70	2e	1a	a1	6f	5d	f9	cd	f3	ce	a1	d6	21 ab cd"
#hexcode :  des해서 나온 16진 코드
hexcode.split('  ')
print(hexcode)

#x1,y1,x2,y2는 방향 벡터를 구할 좌표들 실제로는 key값이될 부분
x1= randint(0,re_width)
y1= randint(0,re_height)
x2= randint(0,re_width)
y2= randint(0,re_height)

#좌표의 rgb값 알아내기
r1,g1,b1 = pix[y1][x1]
r2,g2,b2 = pix[y2][x2]


remainder = len(hexcode)%9
for i in range(0,len(hexcode)-remainder,9):
    tmp = hexcode[i]+hexcode[i+1]+hexcode[i+3]+hexcode[i+4]+hexcode[i+6]+hexcode[i+7]
    print(tmp)
    print(str(int(tmp[0:2],16))+' '+str(int(tmp[2:4],16))+' '+str(int(tmp[4:6],16)))
    r=int(tmp[0:2],16)
    g=int(tmp[2:4],16)
    b=int(tmp[4:6],16)

    #방향벡터 구하기
    vec_r1 = r-r1
    vec_g1 = g-g1
    vec_b1 = b-b1

    vec_r2 = r-r2
    vec_g2 = g-g2
    vec_b2 = b-b2

    msg=msg+str(vec_r1)+' '+str(vec_g1)+' '+str(vec_b1)+' '+str(vec_r2)+' '+str(vec_g2)+' '+str(vec_b2)+' '

    print('==========')

if remainder!=8:
    if remainder == 2:
        q=len(hexcode)//9
        tmp = hexcode[q*9]+hexcode[q*9+1]+'0000'
        print(tmp)
        print(str(int(tmp[0:2],16))+' '+str(int(tmp[2:4],16))+' '+str(int(tmp[4:6],16)))
        r=int(tmp[0:2],16)
        g=int(tmp[2:4],16)
        b=int(tmp[4:6],16)

        #방향벡터 구하기
        vec_r1 = r-r1
        vec_g1 = g-g1
        vec_b1 = b-b1

        vec_r2 = r-r2
        vec_g2 = g-g2
        vec_b2 = b-b2

        msg=msg+str(vec_r1)+' '+str(vec_g1)+' '+str(vec_b1)+' '+str(vec_r2)+' '+str(vec_g2)+' '+str(vec_b2)+' '

    if remainder == 5:
        q=len(hexcode)//9
        tmp = hexcode[q*9]+hexcode[q*9+1]+hexcode[q*9+3]+hexcode[q*9+4]+'00'
        print(tmp)
        print(str(int(tmp[0:2],16))+' '+str(int(tmp[2:4],16))+' '+str(int(tmp[4:6],16)))
        r=int(tmp[0:2],16)
        g=int(tmp[2:4],16)
        b=int(tmp[4:6],16)

        #방향벡터 구하기
        vec_r1 = r-r1
        vec_g1 = g-g1
        vec_b1 = b-b1

        vec_r2 = r-r2
        vec_g2 = g-g2
        vec_b2 = b-b2

        msg=msg+str(vec_r1)+' '+str(vec_g1)+' '+str(vec_b1)+' '+str(vec_r2)+' '+str(vec_g2)+' '+str(vec_b2)+' '


#stegano로 key값과 벡터를 보낸다
#===================================================================================================
#암호화 문장 steganography로 변환
#===================================================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://xn--wb0btwh7t3yibkc86i9tc5x9b.com/stegano.html')
driver.find_element_by_css_selector("input[type='file']").send_keys(r'F:\2020JejuScienceHighSchool\과제연구\test.JPG')

object = driver.find_element_by_id("input_message")
object.send_keys(msg)
btn = driver.find_element_by_id("encode_btn")
btn.click()


print('finish')
