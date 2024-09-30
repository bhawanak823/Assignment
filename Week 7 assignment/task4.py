# Function to remove odd numbers from a list
def remove_uneven(numbers):
    return [num for num in numbers if num % 2 == 0]


# Main program to test the remove_uneven function
def main_remove_uneven_test():
    # Example list of integers
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Calling the function and storing the result
    even_list = remove_uneven(original_list)

    # Printing the original and filtered lists
    print(f"Original list: {original_list}")
    print(f"List with uneven numbers removed: {even_list}")


# Run the main test program
main_remove_uneven_test()