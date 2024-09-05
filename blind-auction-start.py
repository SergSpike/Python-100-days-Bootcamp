from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bider_details = {}


print("Welcome to the secret auction program.")

def highest_bid (find_highest_bider):
  highest_bid = 0
  for bidder in find_highest_bider:
    amount = find_highest_bider[bidder]
    bider_name = bidder
    if amount > highest_bid:
      highest_bid = amount
      winner = bider_name
  print(f"The winners is {winner} with a ammount of ${highest_bid}")
  
  

more_biders = True

while more_biders == True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bider_details[name] = bid
  is_there_another_bider = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if is_there_another_bider == "yes":
     clear()
  else:
    more_biders = False
    clear()
    highest_bid(bider_details)

#print(bider_details)
  

