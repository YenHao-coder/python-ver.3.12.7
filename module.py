#載入內建的sys 模組並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)
#以別名載入內建的sys 模組並取得資訊
import sys as system
print(system.platform)
print(system.maxsize)

#調整搜尋模組的路徑
import sys
sys.path.append("backup")
sys.path.append("module") #在模組的搜尋路徑列表中［新增路徑]
print(sys.path) #印出模組的搜尋路徑 

#建立geometry模組, 載入使用
import geometry1
result=geometry1.distance(1,1,5,5)
print(result)
result=geometry1.slope(1,2,5,6)
print(result)