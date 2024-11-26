#待辦事項1: 建立 1 - 100 間的隨機生成函數
import random
from guess_number_art import logo
def answer_num():
    num_list = list(range(1,101))
    x_num = random.choice(num_list)
    return x_num

#待辦事項2: 建立困難度選擇的函數
def level(difficulty):
    if difficulty == 'easy':
        return easy_level_turns
    elif difficulty == 'hard':
        return hard_level_turns

#待辦事項3: 建立猜數字並提示範圍的函數
def check_answer(num, answer, turns):
    if num > ans:
        print(f"Too high.")
        return turns - 1
    elif num < ans:
        print(f"Too low.")
        return turns - 1
    elif num == ans:
        return print(f"You got it! The answer was {ans}.")

easy_level_turns = 10
hard_level_turns = 5
ans = int(answer_num()) #隨機生成的正確答案
def game():
    print(logo)
    turns = 0
    guess = 0

    print(f"Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.\nThe answer is {ans}") 
    turns = level(input("Choose a difficulty. Type 'easy' or 'hard': ").lower()) #剩餘機會

    while guess != ans:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, ans, turns)
        if turns == 0:
            print("You've run out of guesses. You lose")
            return 
        elif guess != ans:
            print("Guess again.")
game()

        

        






# guess = int(input("Make a guess: ")) #猜測結果
# def guess():
# if guess > ans:
    
#     return "Too high."
# elif guess < ans:
#     return "Too low."
    

