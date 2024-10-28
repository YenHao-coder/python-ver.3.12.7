 # for 迴圈
fruits = ['apple', 'bananas', 'cherry']
for fruit in fruits:
    print(fruit + ' pie')
 # 從1加到100
sum = 0
for number in range(1, 101):
    sum += number
print(sum)
student_score = [180, 124, 165, 173, 189, 169, 146]
 # 隨機生成密碼編輯器:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', "&", '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your passwords?\n"))
number_numbers = int(input("How many numbers would you like in your passwords?\n"))
number_symbols = int(input("How many symbols would you like in your passwords?\n"))

 #Easy Version: 隨機選取字母、數字與符號列表中的字元，並按照順序形成密碼
import random

password = "" # 製作密碼
for character in range(0, number_letters):
    password += random.choice(letters) # 從列表 "letters" 隨機選取字母加入 "password"

for character in range(0, number_numbers):
    password += random.choice(numbers) # 從列表 "numbers" 隨機選取數字加入 "password"

for character in range(0, number_symbols):
    password += random.choice(symbols) # 從列表 "symbols" 隨機選取符號加入 "password"

print(f"Your password is : {password}")

 #Hard Version: 隨機選取字元後，製作成列表，打亂列表排序後並生成密碼
password_list = [] # 製作列表

for character in range(0, number_letters):
    password_list.append(random.choice(letters)) # 從列表 "letters" 隨機選取字母加入列表 "password_list"

for character in range(0, number_numbers):
    password_list.append(random.choice(numbers)) # 從列表 "numbers" 隨機選取數字加入列表 "password_list"

for character in range(0, number_symbols):
    password_list.append(random.choice(symbols)) # 從列表 "symbols" 隨機選取符號加入列表 "password_list"

random.shuffle(password_list) # 打亂列表內排序
print(password_list)

password = "" # 製作密碼

for character in password_list:
    password += character

print(f"Your password is : {password}")