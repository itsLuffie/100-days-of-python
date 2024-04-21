student_height = input("Enter the heights.").split()
sum = 0
for n in range (0, len(student_height)):
    student_height[n]=int(student_height[n])
    sum += int(student_height[n])
avg = sum / (n+1)
print(avg)