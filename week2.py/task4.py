#Asking user for three integer inputs
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate sum, product, and average
sum_numbers = num1 + num2 + num3
product_numbers = num1 * num2 * num3
average_numbers = sum_numbers / 3

# output the results
print(f"Sum: {sum_numbers}")
print(f"Product: {product_numbers}")
print(f"Average: {average_numbers}")

