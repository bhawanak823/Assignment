# Prompt the user to input the cabin class
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").strip().upper()

# Determine the description based on the cabin class
if cabin_class == "LUX":
    description = "Upper-deck cabin with a balcony."
elif cabin_class == "A":
    description = "Cabin above the car deck with a window."
elif cabin_class == "B":
    description = "Windowless cabin above the car deck."
elif cabin_class == "C":
    description = "Windowless cabin below the car deck."
else:
    description = "Invalid cabin class."

# Print the description
print(description)