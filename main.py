#主程式
import sys
sys.path.append("backup")
import backup.point
result=backup.point.distance(3,4)
print("距離:", result)
import backup.line
result=backup.line.slope(1,1,3,3)
print("斜率:", result)
#封包別名
import backup.line as line
result=line.slope(1,1,3,3)
print("斜率:", result)