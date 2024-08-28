rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(user_value)

if user_value == 0:
    print(rock)
elif user_value == 1:
    print(paper)
elif user_value == 2:
    print(scissors)
else:
    print("Invalid Input")


#Logic for computer random nuber choosing

import random 
computer_value = random.randint(0,2)

if user_value <= 2:
    print(f"computer choose {computer_value}")
    if computer_value == 0:
        print(rock)
    elif computer_value == 1:
        print(paper)
    elif computer_value == 2:
        print(scissors)
else:
    print("Invalid Input")



#Logic for win or draw determination 

if user_value >= 3 and computer_value >= 3:
    print("You Choose wrong number. Game over")
elif user_value == 0 and computer_value == 2:
    print("You win")
elif user_value == 2 and computer_value == 1:
    print("You win")
elif user_value == 1 and computer_value == 0:
    print("You win")
elif user_value == computer_value:
    print("Draw")
else:
    print("You lose")