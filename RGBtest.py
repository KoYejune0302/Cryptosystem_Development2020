from PIL import Image
import numpy as np
import math

f=open('img_information.txt','w')

img_name='test.jpg'
im=Image.open(img_name)

width, height=im.size
ratio = height / width
re_width=100
re_height = round(ratio*re_width)
re_im = im.resize((re_width, re_height))


pix = np.array(re_im)
print(re_im.size)
print(pix[50][50])

for i in range(0,re_width,1):
      for j in range(0,re_height,1):
            r,g,b=pix[i][j]
            f.write('x좌표 : '+str(i)+' y좌표 : '+str(j)+' -> '+str(r)+','+str(g)+','+str(b)+','+'\n')
f.close()


'''
f=open('rgb.txt','w')
for r in range(256):
      for g in range(256):
            for b in range(256):
                  f.write('('+str(r)+','+str(g)+','+str(b)+') ->'+str(math.sqrt(r**2+g**2+b**2))+'\n')
f.close()
'''
