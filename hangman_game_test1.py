word_list = ['aardvark', 'baboon', 'camel']

import random
chosen_word = random.choice(word_list)
print(chosen_word)

Placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    Placeholder += "_"
print(Placeholder)

correct_letters = []

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You Win!")