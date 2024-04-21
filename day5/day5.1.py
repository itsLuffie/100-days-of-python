student_height = input("Enter the heights.").split()
total_height = 0
number_of_students=0
for height in student_height:
    total_height += int(height)
for students in student_height:
    number_of_students += 1

average = (total_height/number_of_students)
print(average)