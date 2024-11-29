# 展示圖示
from higher_lower_art import logo, vs
from pokemon_speed_data import data
import random
print(logo)

def formate_data(poke):
    """將資料格式轉為可列印格式"""
    name = poke["name"]
    descript = poke["descript"]
    ability = poke["ability"]
    return f"{name}, {descript}, {ability}"

def check(user_guess, speed_1, speed_2 ):
    """接收使用者猜測與速度值並回傳使用者猜測是否正確"""
    ## 使用if...描述猜測是否正確
    if speed_1 > speed_2:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
should_continue = True
poke_2 = random.choice(data)

while should_continue:
    # 從資料庫隨機選取
    # 使得原本的第二位變成下次開始的第一位
    poke_1 = poke_2
    poke_2 = random.choice(data)
    if poke_1 == poke_2:
        poke_2 = random.choice(data)

    print(f"Compare A: {formate_data(poke_1)}.")
    print(vs)
    print(f"Against B: {formate_data(poke_2)}.")

    # 詢問使用者的猜測
    guess = input("Who has more speed? Type 'A' or 'B': ").lower()

    # 清除畫面
    print('\n' * 20)

    # 查看使用者的猜測是否正確
    ## 取得每一個速度值
    sp_1 = poke_1['speed']
    sp_2 = poke_2['speed']
    is_correct = check(guess, sp_1, sp_2)

    # 針對猜測提供使用者反饋
    # 計分
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        should_continue = False

# 遊戲重複執行

