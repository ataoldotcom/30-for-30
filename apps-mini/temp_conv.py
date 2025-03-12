## Convert a temperature collected in farenheit to Celcius + Kelvin
## to change this up from the mph one, use functions.

print("\nWelcome to the Temp Converter\n")


def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,4)

def c_to_k(fahrenheit):
    kelvin = ((fahrenheit - 32) * 5/9) + 273.15
    return round(kelvin,4)

while True:    
    #temp_us = round(float(input("Enter the temperature in farenheit: \n")),2)
    #temp_cel = f_to_c(temp_us)
    #temp_k = c_to_k(temp_us)
    
    try:
        temp_us = round(float(input("Enter the temperature in degrees farenheit: \n")),2)
        temp_cel = f_to_c(temp_us)
        temp_k = c_to_k(temp_us)

        #temp_us = round(float(input("What is the temperature in farenheit: \n")),2)
        print(f"\n{'Degrees Fahreneheit:':<20} {temp_us}")
        print(f"{'Degrees Celsius:':<20} {temp_cel}")
        print(f"{'Degrees Kelvin:':<20} {temp_k}\n")
        break

    except ValueError:
        print("Please enter a valid numeric temperature\n")
        continue