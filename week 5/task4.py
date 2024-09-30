
cities = []
# Use a for loop
for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)

# Use a for loop
print("\nThe cities you entered are:")
for city in cities:
    print(city)
