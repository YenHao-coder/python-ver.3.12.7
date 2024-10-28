 #隨機Random()生成英文單詞: Head, Tails
import random
word0 = random.choice(['Heads', 'Tails'])
print(word0) #方法 1

word1 = random.randint(0,1)
if word1 == 0:
    print('Heads')
else:
    print('Tails') #方法 2
 #誰來買單
friend = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']
print(random.choice(friend)) #方法 1

random_index = random.randint(0, 4)
print(friend[random_index]) #方法2

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"] # 數列結合的位置
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0]) # 第1數列
print(dirty_dozen[1]) # 第2數列
print(dirty_dozen[1][2]) # 第2數列的第3格字串
print(dirty_dozen[1][3]) # 第2數列的第2格字串
print(dirty_dozen[1][1]) # 第2數列的第1格字串
 #猜拳遊戲

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
L1 = [rock, paper, scissors]
Player1_choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n'))
if Player1_choice > 2 or Player1_choice < 0:
    print("You typed an invalid number. You lose!") #輸入不合規定的數字時...
else:
    print(L1[Player1_choice])

Computer_choice = random.randint(0, 2)
print('Computer chose\n'+L1[Computer_choice])

if Player1_choice > 2 or Player1_choice < 0:
    print("You typed an invalid number. You lose!") #輸入不合規定的數字時...
elif Computer_choice == Player1_choice: #平手時...
    print("It's a Draw")
elif Computer_choice == 0 and Player1_choice == 2: #石頭贏剪刀...
    print("You lose!")
elif Computer_choice == 2 and Player1_choice == 0:
    print("You win!")
elif Computer_choice < Player1_choice:
    print("You win!")
else:
    print("You lose!") 