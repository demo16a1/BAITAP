#viết chương trình tính BMI
a=float(input('nhập cân nặng ='))
b=float(input('nhập chiều cao ='))
BMI=a/(b*b)
if BMI<18.5:
    print('bạn đang thiếu cân')
elif BMI>18.5 and BMI<24.99:
    print('bạn đủ cân')
else:
    print('bạn đang thừa cân')