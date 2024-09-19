def check_zander_length():
    # Define the legal size limit
    legal_size = 42

    # Prompt the user to enter the length of the zander
    try:
        length = float(input("Enter the length of the zander in centimeters: "))

        # Check if the length is less than the legal size limit
        if length < legal_size:
            # Calculate how many centimeters short the zander is
            short_by = legal_size - length
            print(f"The zander is below the legal size limit.release it back into the lake.")
            print(f"The fish is {short_by:.2f} centimeters short of the limit.")
        else:
            print("The zander meets the legal size limit and can be kept.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Run the function
check_zander_length()
