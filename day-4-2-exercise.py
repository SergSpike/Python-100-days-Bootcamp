# Split string method
names_string = input("Give me everybody's names, separated by a comma and sapce correcty. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(names)
lenth_of_list = len(names)
#print(lenth_of_list)

import random
random_number = random.randint(0,lenth_of_list-1)
#print(random_number)

print(f"{names[random_number]} will pay the bill")

