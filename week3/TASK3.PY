def check_hemoglobin_level(gender, hemoglobin):
    # Define normal ranges for adult females and males
    ranges = {
        'female': (117, 155),
        'male': (134, 167)
    }

    # Convert gender to lowercase to handle case insensitivity
    gender = gender.lower()

    # Check if the gender is valid
    if gender not in ranges:
        return "Invalid gender. Please specify 'female' or 'male'."

    # Get the normal range for the specified gender
    min_hemoglobin, max_hemoglobin = ranges[gender]

    # Determine the hemoglobin status
    if hemoglobin < min_hemoglobin:
        return "Your hemoglobin level is low."
    elif hemoglobin > max_hemoglobin:
        return "Your hemoglobin level is high."
    else:
        return "Your hemoglobin level is normal."


def main():
    print("Welcome to the Hemoglobin Level Checker!")

    # Get user input
    gender = input("Please enter your biological gender (female/male): ").strip()

    try:
        hemoglobin = float(input("Please enter your hemoglobin level (g/L): ").strip())
    except ValueError:
        print("Invalid input for hemoglobin level. Please enter a valid number.")
        return

    # Check and display the hemoglobin status
    result = check_hemoglobin_level(gender, hemoglobin)
    print(result)


if __name__ == "__main__":
    main()
