import random

# Generate a 3-digit combination (each number between 0 and 9)
def generate_3_digit_combination():
    combination = [random.randint(0, 9) for _ in range(3)]
    return combination

# Generate a 4-digit combination (each number between 1 and 6)
def generate_4_digit_combination():
    combination = [random.randint(1, 6) for _ in range(4)]
    return combination

# Generate and display both combinations
three_digit_code = generate_3_digit_combination()
four_digit_code = generate_4_digit_combination()

print("3-Digit Combination (0-9):", three_digit_code)
print("4-Digit Combination (1-6):", four_digit_code)

