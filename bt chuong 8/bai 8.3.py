# giải phương trình bậc nhất
a=int(input('a ='))
b=int(input('b ='))
if a==0 and b==0:
    print('phương trình có vô số nghiệm')
elif a==0 and b!=0:
    print('phuong trình vô nghiệm')
else:
    print("phương trình có nghiệm x =",-b/a)

