import os
from art import logo


print(logo)

operators = """+
-
*
/"""
resume=True
re = True
repeat= ''
def calculator(f_num,operator,l_num):
    
    if operator == "+":
        add = f_num+l_num
        print(f"{f_num} + {l_num} = {add}")
        return add

    elif operator == "-":
        sub = f_num - l_num
        print(f"{f_num} - {l_num} = {sub}")
        return sub

    elif operator == "*":
        mul = f_num * l_num
        print(f"{f_num} * {l_num} = {mul}")
        return mul 

    elif operator == "/":
        div = f_num /l_num
        print(f"{f_num} / {l_num} = {div}")
        return div 
    

while resume:
    result = calculator(f_num=int(input("What's the first number?: ")),
        operator=input(f"{operators}\nPick an operator: "),
        l_num=int(input("What's the next number?: ")))
    while re:
        repeat = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. ")
        if repeat == 'y':
            
            new_calc = calculator(f_num=result,
                                operator=input(f"{operators}\nPick an operator: "),
            l_num=int(input("What's the next number?: ")))
            result = new_calc
        elif repeat == 'n':
            os.system('clear')
            re = False
            print(logo)

    