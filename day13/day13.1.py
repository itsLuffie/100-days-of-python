# producing bug




# # Describe Problem
# def my_function():
#     for i range (1, 20): # change the 20 to 21
#         if i == 20:
#             print ("You got it")
# my_function

# Reproduce the Bug
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1,6)     # change the range to 0 to 5
# print(dice_imgs[dice_num])



# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: #make it to include 1994 in the condition
#     print("you are millenial.")
# elif year > 1994: # for that add an = sign in any place for 1994
#     print("You are a Gen Z.")



# Fix the Errors
# age = input("How old are you?") #take the input as int 
# if age > 18:
# print("You can drive at age {age}.") #indent the print statement and add f infront of the print statement

# Print is you Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # There should be 1 = sign instead of 2
# total_words = pages * word_per_page
# print(total_words)


# Use a Debugger
# def mutate(a_list): 
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item) #this should be inside the loop
#     print(b_list)
    
# mutate([1,2,3,5,8,13])