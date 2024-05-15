

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide a valid input."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Your name is {formatted_f_name} {formatted_l_name}."



    
print(format_name(input("Enter your first name.\n"), input("Enter your last name.\n")))