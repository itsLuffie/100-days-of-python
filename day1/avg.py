print("Enter the 3 numbers")
sum = 0
a = 0
for i in range(3):
    a = int(input())
    sum += a

print(round(sum/3,3))