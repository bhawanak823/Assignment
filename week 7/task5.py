import math


# Function to calculate the unit price per square meter of pizza
def pizza_unit_price(diameter_cm, price_euros):
    # Convert diameter from centimeters to meters and calculate the radius
    radius_m = diameter_cm / 2 / 100
    # Calculate the area of the pizza in square meters
    area_m2 = math.pi * (radius_m ** 2)
    # Calculate and return the price per square meter
    return price_euros / area_m2


# Main program to compare two pizzas
def main():
    # Input details for the first pizza
    diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
    price1 = float(input("Enter the price of the first pizza (euros): "))

    # Input details for the second pizza
    diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
    price2 = float(input("Enter the price of the second pizza (euros): "))

    # Calculate the unit prices using the function
    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    # Print out the unit prices for reference
    print(f"\nUnit price of first pizza: {unit_price1:.2f} €/m²")
    print(f"Unit price of second pizza: {unit_price2:.2f} €/m²")

    # Determine which pizza offers better value for money
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


# Run the main program
main()