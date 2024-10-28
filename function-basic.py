#定義函式
#函式內部程式碼: 若是沒有函式呼叫就不會執行
def multiply(n1, n2):
    print(n1*n2)
    return 
#呼叫函式
multiply(3,4)
#函式呼叫並不是回傳值，回傳值未註明即是None
value=multiply(3,4)
print(value) 
#任意回傳資料:回傳值為10
def multiply(n1, n2):
    print(n1*n2)
    return 10
value=multiply(3,4)
print(value) 
#任意回傳資料:回傳值為n1*n2
def multiply(n1, n2):
    print(n1*n2)
    return n1*n2
value=multiply(3,4)
print(value)
#任意回傳資料:不印出結果而是直接回傳值為n1*n2
def multiply(n1, n2):
    return n1*n2
value=multiply(3,4)+multiply(10,5)
print(value) 
#程式包裝:同樣程式碼在函式內可反複呼叫，不需要重新撰寫
def calculate():
    sum=0
    for n in range(1,11):
        sum=sum+n
    print(sum)
calculate()
#加入參數增加函式可操作性
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)
calculate(10)
calculate(20)