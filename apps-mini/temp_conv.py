## Convert a temperature collected in farenheit to Celcius + Kelvin
## to change this up from the mph one, use functions.

print("\nWelcome to the Temp Converter\n")


def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,4)
def c_to_k(fahrenheit):
    #enter fomula
    kelvin = ((fahrenheit - 32) * 5/9) + 273.15
    return round(kelvin,4)

#may need to move this in the loop
#temp_cel = f_to_c(temp_us)
#temp_k = c_to_k(temp_us)

#try-except error handling
while True:    
    temp_us = round(float(input("What is the temperature in farenheit: \n")),2)
    temp_cel = f_to_c(temp_us)
    temp_k = c_to_k(temp_us)
    
    try:
        #temp_us = round(float(input("What is the temperature in farenheit: \n")),2)
        print(f"\nDegrees Fahreneheit: {temp_us}")
        print(f"Degrees Celsius: {temp_cel}")
        print(f"Degrees Kelvin: {temp_k}")
        break

    except ValueError:
        print("Please enter a valid numeric temperature")
        continue