import gavel_art
print(gavel_art.logo)

# 待辦事項1: 詢問姓名與出價金

# 待辦事項2: 將姓名與出價金建立成字典 :{姓名:出價金}


# 待辦事項3: 詢問還有其他出價者需要記錄
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
    Name = input('What is your name?: ')
    Price = int(input('What is your bid?: $'))
    bids[Name] = Price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" *20)


# 待辦事項4: 找出最高的出價者與出價金









