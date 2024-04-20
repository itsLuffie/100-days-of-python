name_string = input("Enter everyones name: ")
name = name_string.split(", ")

import random
x = random.randint(0,len(name))
print (f"The person paying bill will be {name[x]}.")