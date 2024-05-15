import time
import random
name = input("Enter you name.\n")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
array = []
array += str(name)

def randomizer():
    add = ""
    n=0
    while n<len(array):
        word = random.choice(letters)
        if word == array[n]:
            n+=1
            
            add += word
            print(f"Your name is {add}")
            time.sleep(1/60)        
        else:
            
            print(f"Your name is {add}{word}")
            time.sleep(1/60)

randomizer()