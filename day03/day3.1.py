# check if the person can vote or not
age = int(input("Enter your age:\n"))
if age < 18:
    print("You can vote")
else:
    print("You are not legible to vote")