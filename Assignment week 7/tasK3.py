# Function to calculate the sum of a list of integers
def sum_of_list(numbers):
    return sum(numbers)


# Main program to test the sum_of_list function
def main_sum_test():
    # Example list of integers
    test_list = [10, 20, 30, 40, 50]

    # Calling the function and storing the result
    total_sum = sum_of_list(test_list)

    # Printing the result
    print(f"The sum of {test_list} is {total_sum}.")


# Run the main test program
main_sum_test()