#tính kết quả biểu thức
print('nhập số nguyên n và số thực x từ bàn phím')
n=int(eval(input('n =')))
x=float(eval(input('x =')))
P=int(1)
Q=int(1)
#i=int(0)
bt1=x*x+x+1
bt2=x*x-x+1
for i in range(n):
    P*=bt1
    Q*=bt2
A=float(P+Q)
print("A = %0.2f"%A)