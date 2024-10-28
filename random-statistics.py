#隨機模組
import random
# 隨機選取
data1=random.choice([1,5,6,10,20])
print(data1)
#隨機選取3筆
data2=random.sample([1,5,6,10,20],3)
print(data2)
#隨機調換順序 (洗牌)
data3=[1,5,8,20]
random.shuffle(data3)
print(data3)
#隨機取得亂數
data4=random.random() #0~1之間隨機亂數
print(data4)
data5=random.uniform(0.0, 1.0) #0~1之間隨機亂數
print(data5)
#取得常態分配亂數
#平均數100，標準差10，得到的資料多數在90~110之間
data6=random.normalvariate(100, 10)
print(data6)
#平均數0，標準差5，得到的資料多數在 -5 ~ 5 之間
data7=random.normalvariate(0, 5)
print(data7)
#統計模組
#取得平均數
import statistics as stat
data8=stat.mean([1, 4, 5, 8, 2, 3, 100])
print(data8)
#取得中位數
data9=stat.median([1, 4, 5, 8, 2, 3, 100])
print(data9)
#取得標準差
data10=stat.stdev([1, 4, 5, 8, 2, 3, 100])
print(data10)