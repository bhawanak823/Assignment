def convert_to_kg_g(talent, pound, lot):
    # Conversion rates
    lot_to_grams = 13.3
    pound_to_lots = 32
    talent_to_pound = 20

    # Convert the total mass to grams
    total_grams = (talents * talent_to_pound * pound_to_lots * lot_to_grams) + \
                  (pounds * pound_to_lots * lot_to_grams) + \
                  (lots * lot_to_grams)

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