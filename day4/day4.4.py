#build rock paper scissor
import random

user = int(input("Enter you decision.\n0. Rock\n1. Paper\n2. Scissor\n"))

computer = random.randint(0,2)
if user == computer:
    print("It's a tie")
if user>computer or user ==computer+2:
    print("You win.")
if user<computer or user == computer-2:
    print("You lose")
