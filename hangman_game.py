word_list = ['aardvark', 'baboon', 'camel']
 # Todo1 - Randomly choose a word
import random
chosen_word = random.choice(word_list)
print(chosen_word)

 # Todo2 - Ask the user to guess a letter and asign their ansewr to a variable call guess.

# guess = input("Guess a letter: ").lower()

#  # Todo3 - Check if letter the user guessed is one of the letter in the chosen_word. Print "Right!" if  it is."Wrong!" if it's not.
# for letter in chosen_word:
#     if letter == guess:
#         print('Right')
#     else:
#         print('Wrong')

 # ToDo-1: Create a "Placeholder" with the same number of blanks as the chosen_word
Placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    Placeholder += "_"
print(Placeholder)

# guess = input("Guess a letter: ").lower()
 # Todo-2: Create a "display" that puts the guess letter in the right position and _ in the wrong position
 # diplay = ""
# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"
# print(display)

 # Todo-1 Use a while loop to let the user guess again
correct_letters = []

game_over = False

lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

 # Todo-2 Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        
        else:
            display += "_"     

    print(display)
    
    if guess not in correct_letters:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You Win!")
    
    print(f'剩餘次數: {lives} 次')
# Todo-1 Create a variable called "lives" to keep track of the number of the lives left
# Set lives equal to 6.
# Todo-2 If guess is not a letter in the chosen_word, then reduce lives by 1
# If lives goes down to 0 then the game should end, and it should print "You lose."
# Todo-3 Print the ASCII Art from the list stages that corresponds to the current number of lives the user has remaining
