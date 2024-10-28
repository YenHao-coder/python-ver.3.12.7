 # 條件式
print('Welcome to the rollercoaster!')
height = int(input("What is your height in cm? "))
if height>=120:
     print('You can ride the rollercoaster')
else:
    print('Sorry you have to grow taller before you can ride. ')
  # 餘數
  # 偶數判斷方法
number = int(input("What is the number you want to check? "))
if number % 2 != 0:
    print("It's odd number! ")
else:
    print("It's even number! ")
# 不同年齡的雲霄飛車票價判斷方法
print('Welcome to the rollercoaster!')
height = int(input("What is your height in cm? "))
if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input("How old are you? "))
    if age <= 12:
        print("You need to pay $5 ")
    elif 12 < age <= 18:
        print("You need to pay $7 ")
    else:
        print("You need to pay $12 ")
else:
    print('Sorry you have to grow taller before you can ride. ')
 #不同年齡雲霄飛車價格外,詢問是否購買照片
print('Welcome to the rollercoaster!')
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input("How old are you? "))
    if age <= 12:
        print("You need to pay $5 ")
        bill = 5
    elif 12 < age <= 18:
        print("You need to pay $7 ")
        bill = 7
    else:
        print("You need to pay $12 ")
        bill = 12
    wnats_photo = input("Do you want to have a photo take? Type y for yes and n for No. ")
    if wnats_photo == "y":
        bill += 3 # 增加 3元
    print(f"Your final bill is ${bill}")
else:
    print('Sorry you have to grow taller before you can ride. ')
# 訂購pizza流程:
print("Welcome to Python Pizza Deliveries! ")
bill = 0
size = input("What size pizza do you want? s, m or l: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")
if size == "s":
    print("Small size is $15 ")
    bill += 15
elif size == "m":
    print("Medium size is $20 ")
    bill += 20
elif size == "l":
    print("Large size is $25 ")
    bill += 25
else:
    print("You typed the wrong inputs. ")
if pepperoni == "y":
    if size != "s":
        bill += 2
        print("added pepperoni plus $2")
    else:
        bill +=3
        print("added pepperoni plus $3")
if extra_cheese == "y":
    bill += 1
    print("added extra cheese plus $1")
print(f"Your final bill is :{bill}")
 #寶藏島走迷宮
print("Welcome to Treasure Island\nYour mission is to find treasure")
choice_1 = input('You\'re at a cross road. Where do you want to go?\n\bType "left" or "right". \n').lower() #.lower()字串中的大寫符號轉換成小寫
if choice_1 == "left":
    choice_2 = input('''You\'ve come to a lake.
    There is a island un the middle of the lake.
    Type "swim" to swim across.
    Type "wait" to wait for a boat. ''').lower()
    if choice_2 == "wait":
        choice_3 = input('''You arrive at the island unharmed.
        There is house with 3 doors. One red, 
        One yellow and one blue. 
        Which colour do you choose?''').lower()
        if choice_3 == "red":
            print("It's a rooom full of fire. Game Over.")
        elif choice_3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice_3 == "blue":
            print("You enter a room of beast. Game Over.")
        else:
            print("You chose a door that dosen't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell in to  a hole. Game Over! ")