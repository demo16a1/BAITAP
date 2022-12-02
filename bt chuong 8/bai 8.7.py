#tính tiền điện pải trả của hộ gia đình
x=int(eval(input('x =')))
if x<=50:
    print("tiền điện phải trả là :",x*1.678)
elif x>50 & x<=100:
    print("tiền điện phải trả là :",50*1.678+(x-50)*1.734)
elif x>100 & x<=200:
    print("tiền điện phải trả là :",50*1.678+50*1.734+(x-100)*2.014)
elif x>200 & x<=300 :
    print("tiền điện phải trả là :",50*1.678+50*1.734+100*2.014+(x-200)*2.536)
elif x>300 & x<=400 :
    print("tiền điện phải trả là :",50*1.678+50*1.734+100*2.014+200*2.536+(x-300)*2.834)    
else:
    print("tiền điện phải trả là :",50*1.678+50*1.734+100*2.014+200*2.536+300*2.834+400*2.927)