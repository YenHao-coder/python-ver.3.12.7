r=float(input('請輸入今年收入淨額: ')) #請輸入今年收入淨額: 
if r>=2000000:
    tax=r*0.3
elif 1000000<=r<=1999999:
    tax=r*0.21
elif 600000<=r<=999999:
    tax=r*0.13
elif 300000<=r<=599999:
    tax=r*0.06
else:
    tax=0
print('付稅金額:'+str(tax)+' 元') #付稅金額: 元