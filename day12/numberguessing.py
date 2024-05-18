#choose among easy and hard 
#if easy then 10 life
#if hard then 5 life
import random
import art
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
is_game_end = False

def guessing(guess, answer):
    
    if turns == 0:
        is_game_end = True
        print(f"You've run out of guesses, you lose")
        

    
    if guess < answer:
        print(f"Too Low\nGuess again")
    elif guess > answer:
        print(f"Too high\nGuess again")
    if guess == answer:
        is_game_end = True
        print(f"You got it! The answer is {guess}")
        


def set_difficulty():
    if level == "easy":
        global turns
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
    



print (art.logo)
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

answer = random.randint(1,100)


guess = int(input("Make a guess: "))
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")


while not is_game_end:
    guessing(guess, answer)