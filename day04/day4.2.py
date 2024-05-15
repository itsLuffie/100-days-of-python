name_string = input("Enter everyones name: ")
name = name_string.split(", ")

import random
x = random.choice(name)         #choice function will directly pick the name from the function
print(f"{x} will pay")

# below function can be used to run without choice function
# paying_person = random.randint(0,len(name)-1)
# print (f"The person paying bill will be {name[paying_person]}.")