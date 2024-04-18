def digit_sum(n):
    """Function to find the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def sum_of_multiples(num1, num2):
    """Function to find the sum of the output of multiples of two numbers."""
    product = num1 * num2
    return digit_sum(product)

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating the sum of multiples and printing the result
result = sum_of_multiples(num1, num2)
print("The sum of the output of multiples of {} and {} is: {}".format(num1, num2, result))
