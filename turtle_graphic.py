from turtle import Turtle, Screen
timmy = Turtle() # car_(object) = carblueprint()_(class)
print(timmy)
timmy.shape("turtle") 
timmy.color("brown") # car_(object).color_(method)
timmy.forward(100) # car_(object).move_(method)

my_screen = Screen() # car_(object) = carblueprint()_(class)
print(my_screen.canvheight) # car_(object).speed_(attributes)
my_screen.exitonclick() # 點擊視窗離開: car_(object).stop_(method)

from prettytable import PrettyTable
table = PrettyTable() # 新增一個物件 type
table.add_column("Pokemon name", ["Pikachu", "Snorlax","Aerodactyl"]) # 新增加 1 行
table.add_column("Type", ["Electric", "Normal", "Rock Flying"]) # 新增加 1 行

table.align = "l" # 文字靠左對齊 
print(table)