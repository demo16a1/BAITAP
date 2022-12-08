# tính năm âm lịch từ năm dương lịch
a=int(input('nhập năm: '))
can =a%10
chi = a%12
if can=0:
    print('canh')
elif can=1:
    print('tân')
elif can=2:
    print('nhâm')
elif can=3:
    print('quý')
elif can=4:
    print('giáp')