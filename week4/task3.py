#
min_number = 0
max_number = 0

while True:
    number = int(input ("Enter a number:"))
    if number == "":
        break
    numberInInt = int(number)
    if int(number) < min_number or min_number == 0:
        min_number = number
    elif int(number) > max_number or max_number == 0:
        max_number = number
        print(f"smallest number is: {min_number}")
        print(f"largest number is : {max_number}")



