def convert_to_kg_g(talents, pounds, lots):
    # Conversion rates
    LOT_TO_GRAMS = 13.3
    POUNDS_TO_LOTS = 32
    TALENT_TO_POUNDS = 20

    # Convert the total mass to grams
    total_grams = (talents * TALENT_TO_POUNDS * POUNDS_TO_LOTS * LOT_TO_GRAMS) + \
                  (pounds * POUNDS_TO_LOTS * LOT_TO_GRAMS) + \
                  (lots * LOT_TO_GRAMS)

    # Convert grams to kilograms and grams
    kilograms = int(total_grams // 1000)
    grams = total_grams % 1000

    return kilograms, grams


# Get input from the user
print("Enter the mass in medieval units:")
talents = int(input("Talents: "))
pounds = int(input("Pounds: "))
lots = int(input("Lots: "))

# Convert to kilograms and grams
kilograms, grams = convert_to_kg_g(talents, pounds, lots)

# Output the result
print(f"The total mass is {kilograms} kg and {grams:.2f} grams.")