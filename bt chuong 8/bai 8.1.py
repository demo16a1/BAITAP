#tìm số lớn nhất và số nhỏ nhất
a=input('nhập a =')
b=input('nhập b =')
c=input('nhập c =')
d=input('nhập d =')
max =a
if b>c>max or b>d>max:
    print("số lớn nhất là:",b)
elif c>b>max or c>d>max:
    print("số lớn nhất là:",c)
elif d>c> max or d>b>max:   
    print("số lớn nhất là :",d)
else:
    print("số lớn nhất là:",max)
