import random
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)


display = []
for i in chosen_word:
    display += "_"
print(display)

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter.\n").lower()
        
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game == True
            print("You lose")
            break
    if "_" not in display:
        end_of_game = True
        print("You win")