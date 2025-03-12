##Multiplication/Exponent Table app

print("Welcome to the Multiplication/Exponent Table App")

name = input("What is your name:\t")

while True:
    try:
        number = float(input("What number would you like to work with?:\t"))
        print(f"\nMultiplication Table or {number}\n")
        #need to add print statements for math equations
        break
    except ValueError:
        print("Enter a numberic value only.")