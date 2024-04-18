# Love Calculator
name1= input("Enter your name\n")
name2 = input("Enter their name\n")
combined_string = name1 + name2
combined_string_lower = combined_string.lower()
t = combined_string_lower.count("t")
r = combined_string_lower.count("r")
u = combined_string_lower.count("u")
e = combined_string_lower.count("e")
l = combined_string_lower.count("l")
o = combined_string_lower.count("o")
v = combined_string_lower.count("v")
true = t+r+u+e
love = l+o+v+e
love_score = int(str(true) + str(love))
if love_score >= 90:
    print(f"Your score is {love_score}. Wooho you bot are like coke and mentos.")
elif love_score < 90 and love_score >50:
    print(f"Your score is {love_score} You guys are great together.")
else:
    print(f"Your love calculator value is {love_score}")