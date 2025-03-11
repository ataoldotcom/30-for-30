print("Welcome to the MPH Conversion app\n")

while True:
    try:
        speed = float(input("What is your speed in miles per hour: \n"))
    except ValueError:
        print("Please enter a valid speed")
        continue
    else:
        conversion = speed * 1.6094
        print(f"Your converted speed is: {conversion}")