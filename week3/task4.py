def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    print("Welcome to the Leap Year Checker!")

    # Get user input
    try:
        year = int(input("Please enter a year: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        return

    # Determine if the year is a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()
