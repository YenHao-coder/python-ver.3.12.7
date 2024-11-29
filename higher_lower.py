from higher_lower_art import logo, vs
from pokemon_speed_data import data
import random
     
print(logo) #圖示 Higher Lower
eliminated = [] #已淘汰名單
pick_def = random.randint(0, 23) #隨機指定守擂者
pick_chanllenger = random.randint(0, 23) #隨機指定挑戰者
print(f"Compare A:{data[pick_def]['name']}, {data[pick_def]['descript']}, {data[pick_def]['ability']}") # 描述 守擂者名字, 簡介,能力
while pick_chanllenger == pick_def:
    pick_chanllenger = random.randint(0, 23) #隨機指定挑戰者
print(vs) #圖示 vs.
print(f"Against B:{data[pick_chanllenger]['name']}, {data[pick_chanllenger]['descript']}, {data[pick_chanllenger]['ability']}") # 描述 挑戰者名字, 簡介,能力

while len(eliminated) < (len(data) - 2):     
    sp_d = data[pick_def]['speed'] #寶可夢 A的速度值
    sp_c = data[pick_chanllenger]['speed'] #寶可夢 B的速度值
    score = len(eliminated)
    selected = input('Who has more speed? Type "A" or "B": ').lower() #使用者的選擇
    print("\n" * 20)
    print(logo) #圖示 Higher Lower
    
    if selected == "a" and sp_d > sp_c: #猜對 A贏
        score += 1
        eliminated.append(pick_chanllenger) #加入淘汰名單
        print(f"You're right! Current score: {score}.")
        print(f"Compare A:{data[pick_def]['name']}, {data[pick_def]['descript']}, {data[pick_def]['ability']}") # 指定衛冕者
        

    elif selected == "b" and sp_d < sp_c: #猜對 B贏
        score += 1
        eliminated.append(pick_def) #加入淘汰名單
        pick_def = pick_chanllenger
        print(f"You're right! Current score: {score}.")
        print(f"Compare A:{data[pick_def]['name']}, {data[pick_def]['descript']}, {data[pick_def]['ability']}") # 指定衛冕者

    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        break
    
    pick_chanllenger = random.randint(0, 23)
    while pick_chanllenger == pick_def:
        pick_chanllenger = random.randint(0, 23)
    print(vs) #圖示 vs.
    print(f"Against B:{data[pick_chanllenger]['name']}, {data[pick_chanllenger]['descript']}, {data[pick_chanllenger]['ability']}")
if len(eliminated) == (len(data) - 2):
    print("Congratulation !") #淘汰全部名單的結束詞

    
    




