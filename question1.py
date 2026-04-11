import random

random_num = random.randint(0, 2)

if random_num == 0:
    comp_choice = "S"
elif random_num == 1:
    comp_choice = "K"
else:
    comp_choice = "P"
    
user_choice = input(
    "Enter your choice (S for Stone, K for Knife, P for Paper): "
).upper()

print("Computer chose:", comp_choice)
print("You chose:", user_choice)

if user_choice == comp_choice:
    print("It's a tie! No one wins.")
elif (
    (user_choice == "S" and comp_choice == "K")
    or (user_choice == "K" and comp_choice == "P")
    or (user_choice == "P" and comp_choice == "S")
):
    print("You win!")
else:
    print("Computer wins!")
