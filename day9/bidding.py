import os
bids= {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} whth the bid of {highest_bid}.")

while not bidding_finished:
    name = input("What is your name:\n")
    price = int(input("What's your bidding?\n"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        os.system('clear')



find_highest_bidder(bidding_record= bids)