from PIL import Image
import numpy as np
import math

f=open('img_information.txt','w')

img_name='test.jpg'
im=Image.open(img_name)

width, height=im.size
ratio = width / height
re_height=100
re_width = round(ratio*re_width)
re_im = im.resize((re_width, re_height))


pix = np.array(re_im)
print(re_im.size)
print(pix[50][50])

for i in range(0,re_height,1):
      for j in range(0,re_width,1):
            r,g,b=pix[i][j]
            f.write('x좌표 : '+str(i)+' y좌표 : '+str(j)+' -> '+str(r)+','+str(g)+','+str(b)+','+'\n')
f.close()


#일단 앞에 모두 과정은 안료됬다고 가정
r=12
g=233
b=187
#rgb를 암호화 해서 전송할것
#re_height
#re_width

from random import *

#x1,y1,x2,y2는 방향 벡터를 구할 좌표들
x1= randint(0,re_width)
y1= randint(0,re_height)
x2= randint(0,re_width)
y2= randint(0,re_height)

#좌표의 rgb값 알아내기
r1,g1,b1 = pix[y1][x1]
r2,g2,b2 = pix[y2][x2]

#방향벡터 구하기
vec_r1 = r-r1
vec_g1 = g-g1
vec_b1 = b-b1

vec_r2 = r-r2
vec_g2 = g-g2
vec_b2 = b-b2

#stegano로 key값과 벡터를 보낸다
