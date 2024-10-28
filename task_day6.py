 #定義函式
def my_function():
    print("Hello") #先執行...
print("Bye") #然後執行...

my_function() #呼叫函式
 #走出迷宮: 靠牆邊站後左轉，並沿著右邊移動
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear(): #起始位置靠牆
    move()
turn_left() #無路走左轉

while not at_goal(): #判斷方向沿右走
    if right_is_clear(): #判斷後右轉
        turn_right()
        move()
    elif front_is_clear(): #判斷後直走
        move()
    else:
        turn_left() #無路走左轉