#集合的運算
s1={3,4,5}
# set
print(3 in s1) #判斷3是否存在s1裡面
print(10 in s1) #判斷10是否存在s1裡面
print(10 not in s1) #判斷10是否存在s1裡面
s2={4,5,6,7}
s3=s1&s2 #交集:取兩個集合中，相同資料
print(s3)
s4=s1|s2 #聯集:取兩個集合中的所有資料，但不取重複資料
print(s4)
s5=s1-s2 #差集:從 s1 中減去與 s2 重疊的部分
print(s5)
s6=s1^s2 #反交集: 取兩個集合中，不重疊的部份
print(s6)
s7=set("Hello") #把字串中的字母拆解成集合: set(字串)
print(s7)
print("H" in s7) #判斷"H"是否存在 s7 裡面
print("A" in s7) #判斷"A"是否存在 s7 裡面
#字典的運算: key-value 配對
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])
dic={"apple":"蘋果","bug":"蟲蟲"}
print("apple" in dic) #判斷 key 是否存在
print("test" not in dic) #判斷 key 是否存在
print(dic)
del dic["apple"] #刪除字典中的鍵值對 (key-Value pair)
print(dic)
dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)

