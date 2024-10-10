a=int(input('請輸入 a 的值: ')) #請輸入 a 的值:
b=int(input('請輸入 b 的值: ')) #請輸入 b 的值:
d=int(input('請輸入 d 的值: ')) #請輸入 d 的值:
 #最大值為: 
if (a>b):
    if (a>d):
        print('最大值為a')
    else:
        print('最大值為d')
else:
    if (b>d):
        print('最大值為b')
    else:
        print('最大值為d')
 #找出最大值
a=int(input('請輸入 a 的值: ')) #請輸入 a 的值:
b=int(input('請輸入 b 的值: ')) #請輸入 b 的值:
d=int(input('請輸入 d 的值: ')) #請輸入 d 的值:
s1={a,b,d}
m=max(s1)
print(m)