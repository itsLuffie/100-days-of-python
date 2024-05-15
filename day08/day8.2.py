import math
test_h = int(input("Enter the height of the wall. "))
test_w = int(input("Enter the width of the wall. "))
coverage = 5
def painting_of_wall(height, width, cover):
    area = height* width
    num_of_cans = math.ceil(area/cover)
    print(f"You need total of {num_of_cans} cans.")
    

painting_of_wall(height = test_h, width = test_w, cover = coverage)