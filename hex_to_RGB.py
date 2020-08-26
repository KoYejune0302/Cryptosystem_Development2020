hexcode="f7	f9	70	2e	1a	a1	6f	5d	f9	cd	f3	ce	a1	d6	21 ab cd"
#hexcode :  des해서 나온 16진 코드
hexcode.split('  ')
print(hexcode)
remainder = len(hexcode)%9
for i in range(0,len(hexcode)-remainder,9):
    tmp = hexcode[i]+hexcode[i+1]+hexcode[i+3]+hexcode[i+4]+hexcode[i+6]+hexcode[i+7]
    print(tmp)
    print('==========')

if remainder!=8:
    if remainder == 2:
        q=len(hexcode)//9
        tmp = hexcode[q*9]+hexcode[q*9+1]+'0000'
        print(tmp)
    if remainder == 5:
        q=len(hexcode)//9
        tmp = hexcode[q*9]+hexcode[q*9+1]+hexcode[q*9+3]+hexcode[q*9+4]+'00'
        print(tmp)
