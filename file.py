#儲存檔案
file=open("data1.txt", mode="w", encoding="utf-8") #開啟。指定UTF-8編碼
file.write("Hello File\nSecond Line\n測試中文\n好棒棒") #操作
file.close() #關閉
# with ...as...用法
with open("data2.txt", mode="w", encoding="utf-8") as file:
    file.write("測試中文\n好棒棒")
#讀取檔案
with open("data2.txt", mode="r", encoding="utf-8") as file:
    data2=file.read()
print(data2)
#檔案資料為一行1個數字
with open("data3.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")
#讀取檔案
#把檔案中的數字資料，一行一行讀取出來，並計算總合
sum=0
with open("data3.txt", mode="r", encoding="utf-8") as file:
    for line in file: #一行一行的讀取
        sum+=int(line)
print(sum)
#使用 JSON 格式讀取、複寫檔案
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典
print("name: ", data["name"])
print("version: ", data["version"])
#修改資料
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典
data["name"]="New Name" #修改變數中的資料
#把最新資料富野回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)