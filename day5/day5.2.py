#highest score in the class
# student_scores = 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores.\n").split()
highest_score=0
for score in student_scores:
    if int(score) > int(highest_score):
        highest_score = score
    
print(f"The highest score in the class is: {highest_score}")