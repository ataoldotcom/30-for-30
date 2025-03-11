print("\n\nWelcome to the MPH Conversion app\n")

while True:
    try:
        speed = float(input("What is your speed in Miles per hour: \n"))
    except ValueError:
        print("Please enter a valid speed")
        continue
    else:
        #this is still returning precision float
        #conversion = round(speed * 1.6094,2)
        conversion = (speed * 1.6094)
        print(f"Your speed in Kilometers per hour:\n{round(conversion,2)} Km/H\n")
        break