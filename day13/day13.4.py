for number in range (1,101):
    if number % 3 == 0 or number % 5 == 0: # should use 'and' instead of 'or'
        print("FizzBuzz")
    if number % 3 == 0: # should use elif condition rather than if
        print("Fizz")
    if number % 5 == 0: # should use elif condition rather than if
        print("Buzz")
    else:
        print([number]) # the big bracket should be removed