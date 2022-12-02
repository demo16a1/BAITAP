#chương trình tính và in ra kết quả biểu thức
print('nhập số nguyên n và số thực x từ bàn phím')
n=int(eval(input('n =')))
x=float(eval(input('x =')))
S=1
i=int(0)
bt = x*x+1
while i<n:
    S*=bt
    i+=1
print("S = %0.2f"%S)