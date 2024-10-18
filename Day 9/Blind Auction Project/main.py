import art

# Possible bugs/improvements to fix:
#   1. If bids are equal, only 1st one will be selected
#   2. Bid input can only be an integer.
#   3. Need a way to clear screen after a bid.
#   4. Check for incorrect entries.

print(art.logo)
print("Eugene's app\n")

bid_dictionary = {}

def make_bid():
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bid_dictionary[name] = bid

# TODO-3: Whether if new bids need to be added
keep_biding = True
while keep_biding:
    make_bid()
    keep_biding_yes_no = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if keep_biding_yes_no == "no":
        keep_biding = False
    elif keep_biding_yes_no == "yes":
        print("\n" * 30)
    else:
        print("Error, what did you type?")
# print(bid_dictionary) # check

# TODO-4: Compare bids in dictionary
highest_bidder_name = ""
highest_bid = 0
for bidder in bid_dictionary:
    if bid_dictionary[bidder] > highest_bid:
        highest_bidder_name = bidder
        highest_bid = bid_dictionary[bidder]
    # Note: max(bid_dictionary, key=bid_dictionary.get) can also be used
print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid}")
