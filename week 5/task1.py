import random

# Ask the user how many dice to roll
num_dice = int(input("How many dice do you want to roll? "))

# Initialize sum to zero
total_sum = 1

# using for loop
for _ in range(num_dice):
    roll = random.randint(1,6)  # Rolls a single die (values between 1 and 6)
    total_sum += roll

print(f"The sum of the rolls is: {total_sum}")