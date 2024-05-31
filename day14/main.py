from game_data import data
from art import logo, vs
import random



print (logo)


current_choice = random.choice(data)
next_choice = random.choice(data)
initial_popularity = current_choice['follower_count']
comparision_popularity = next_choice['follower_count']
score = 0
is_game_end = False
print (f"Compare A:{current_choice['name']}, a {current_choice['description']}, from {current_choice['country']}")


print(vs)


print(f"Against B:{next_choice['name']}, a {next_choice['description']}, from {next_choice['country']}")
print(f"Follower Count = {current_choice['follower_count']}")
print(f"Follower Count = {next_choice['follower_count']}")


user_choice = input("Who has more followers? Type 'A' or 'B': ").upper
if user_choice == 'A':
    if initial_popularity > comparision_popularity:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        is_game_end = True
        return f"Sorry, that's wrong. Final score: {score}"
elif user_choice == 'B':
    if initial_popularity < comparision_popularity:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        return f"Sorry, that's wrong. Final score: {score}"