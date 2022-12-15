# Tính năm âm lịch tư năm dương lịch

def tinh_can(nam):
    if nam % 10==0:
        return"canh"
    elif nam %10==1:
        return 'tân' 
    elif nam %10==2:
        return 'nhâm' 
    elif nam %10==3:
        return 'quý' 
    elif nam %10==4:
        return 'giáp' 
    elif nam %10==5:
        return 'ất' 
    elif nam %10==6:
        return 'bính' 
    elif nam %10==7:
        return 'đinh' 
    elif nam %10==8:
        return 'mậu' 
    else: 
        return 'kỷ'

def  tinh_chi(nam):
    if nam%12==0:
        return 'thân'
    elif nam%12==1:
        return 'dậu'
    elif nam%12==2:
        return 'tuất'
    elif nam%12==3:
        return 'hợi'
    elif nam%12==4:
        return 'tý'
    elif nam%12==5:
        return 'sửu'
    elif nam%12==6:
        return 'dần'
    elif nam%12==7:
        return 'mão'
    elif nam%12==8:
        return 'thìn'
    elif nam%12==9:
        return 'tỵ'
    elif nam%12==10:
        return 'ngọ'
    else:
        return 'mùi'
#
n=int(input('nhập vào năm dương:'))
print('năm âm lịch :',tinh_can(n),tinh_chi(n))