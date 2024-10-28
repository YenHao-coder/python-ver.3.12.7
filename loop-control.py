#break 的簡易範例
n1=0
while n1<5:
    if n1==3:
        break
    print(n1) #印出迴圈中的n1
    n1+=1
print("最後的 n1: ", n1) #印出迴圈結束的n1
#continuous 的簡易範例
n2=0
for x1 in range(4):
    if x1%2==0: #x1是偶數
        continue
    print(x1)
    n2+=1
print("最後的 n2: ", n2)
#else的簡易範例
sum1=0
for n3 in range(11):
    sum1+=n3
else:
    print(sum1) #印出1+2+3+...+10的結果
#綜合範例:找出整數平方根
# 輸入9, 得到 3
# 輸入11, 得到 沒有 整數的平方根
n4=input("輸入一個正整數: ")
n4=int(n4) #轉換輸入成數字
for i in range(n4):
    if i*i==n4:
        print("整數平方根", i)
        break #用break強制結束迴圈時，不會執行else區塊
    else:
        print("沒有整數平方根")