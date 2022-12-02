#tính cước xe taxi 
a=int(input('chọn loại xe 4 hay 7 chỗ:'))
b=float(input('nhập số km ='))
c=float(input('nhập thời gian chờ (phút): '))
tien_cuoc = float(0)
tien_di_chuyen = float(0)
if c >=5:
    tien_cho=(c-5)*0.8
else:
    tien_cho=0
if a == 4:
    if b <=0.8:
        tien_di_chuyen = 11000
    elif b <=20:
        tien_di_chuyen = 11000+(20-b)*12100
    else:
        tien_di_chuyen= 11000+(20-0.8)*12100+(b-20)*10000
    tien_cuoc= tien_cho+tien_di_chuyen
    print("Cước phí xe tacxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
#----------------------------------------------------------------------
if a == 7:
    if b <=0.8:
        tien_cuoc=tien_cho + 13000
    elif b <=30:
        tien_cuoc=tien_cho + 13000+(30-b)*14100
    else:
        tien_cuoc = tien_cho + 13000 +(30-0.8)*14100+(b-30)*12000
    print("Cước phí xe tacxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)
        