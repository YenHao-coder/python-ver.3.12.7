#有序可變動列表 List
grades=[12,60,15,70,90]
grades[0]=55 #把55放入列表第0位
print(grades)
print(grades[0]) #索引列表第0位
print(grades[1:4]) #包含1到3不包含4
grades[1:4]=[] #連續刪除列表中從1到3不包含4的資料
print(grades)
grades=grades+[12,33] #加入列表後面
print(grades)
length=len(grades) #取得列表的長度len(列表資料)
print(length)
data=[[3,4,5],[6,7,8]]
print(data)
print(data[0][1])
data[0][0:2]=[5,5,5]
print(data)
#有序不可變動列表 Tuple
data=(3,4,5)
print(data[0:2])
data[0]=5 #錯誤:Tuple的資料不可以變動
print(data)
