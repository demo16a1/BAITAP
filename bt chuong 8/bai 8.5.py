#viết chương trình xét năm nhập vào có phải năm nhuận 
print("nhập năm x từ bàn phím")
x=int(input('x ='))
if ((x%4==0) and (x%100!=0)):
    print(x, "là năm nhuận")
elif x%400==0:
     print(x, "là năm nhuận")
else:
    print(x, 'không là năm nhuận')
