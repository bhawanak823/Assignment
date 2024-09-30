
num = []

#use while loop
while True:
    user_input = input("Enter a number (or press Enter to finish): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        num.append(number)
    except ValueError:
        print("Please enter a valid number.")

# numbers in descending order
num.sort(reverse=True)

# Print the top five greatest numbers
top_five = num[:5]

print("The five greatest numbers are:")
for num in top_five:
    print(num)
