#參數預設資料
def power(base, exp):
    print(base**exp)
power(3,2)
#power(4) 未設定exp無法執行
#設定參數預設資料
def power(base, exp=0):
    print(base**exp)
power(3,2)
power(4)
#使用參數名稱對應
def divide(n1, n2):
    print(n1/n2)
divide(2,4)
divide(n2=2, n1=4)
#無限/不定參數資料: Tuple
def avg(*ns):
    print(ns)
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)
#無限/不定參數資料: 加入for迴圈
def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns))
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)