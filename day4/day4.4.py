#build rock paper scissor
import random


user = int(input("Enter you decision.\n1. Rock\n2. Paper\n3. Scissor\n"))

computer = int(random.randint(0,2))
if computer == user-1:
    print("It's a tie")
if computer == user-2 or computer==user+1:
    print("You win.")
if computer == user or computer==user+3:
    print("You lose")
