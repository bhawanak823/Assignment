def is_prime(number):
    # Numbers less than or equal to 2 are not prime
    if number <= 2:
        return False

    # Check divisibility from 2 up to the square root of the number
    for i in range(2, int(number ** 0.5) + 2):
        if number % i == 0:
            return False

    # If no divisor was found, the number is prime
    return True

# Ask the user for an integer
try:
    num = int(input("Enter an integer: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
