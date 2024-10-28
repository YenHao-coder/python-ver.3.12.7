#數字運算
x=3/6 #小數除法
print(x)
x=3//6 #整數除法
print(x)
x=2**3 #2的3次方
print(x)
x=2**0.5 #2的根號
print(x)
x=7%3 #7除以3的餘數
print(x)
x=2+3
print(x)
x=x+1 #將變數中的數字+1
x+=1 #x=x+1
x-=1 #x=x-1
x*=1 #x=x*1
print(x)
#字串運算
s="Hello"
print(s)
s="Hell\"o" #\跳脫
print(s)
s="Hello"+"World" #字串串接
print(s)
s="Hello" "World" #字串串接
print(s)
s="Hello\nWorld" #\n換行
print(s)
s="""Hello


World""" #3個雙引號可任意換行
print(s)
s="Hello"*3+"World" #Hello重複3次
print(s)
s="Hello" #字串會對內部的字元編號(索引)，從0開始算起
print(s[0]) #字元0號
print(s[1:4]) #包含1不包含結尾
print(s[1:]) #字元1起包含結尾
print(s[:4]) #包含所有字元不包含結尾