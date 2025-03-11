## Convert a temperature collected in farenheit to Celcius + Kelvin
## to change this up from the mph one, use functions.

print("\nWelcome to the Temp Converter\n")


def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,4)
def c_to_k():
    #enter fomula
    #kelvin = ()
    return round(kelvin,4)

#may need to move this in the loop
temp_cel = f_to_c(temp_us)
temp_k = ()

#try-except error handling
while True:    
    try:
        temp_us = round(float(input("What is the temperature in farenheit: \n")),2)
        print("Degrees Fahreneheit: ")
        print("Degrees Celsius: ")
        print("Degrees Kelvin: ")
        break

    except ValueError:
        print("Please enter a valid numeric temperature")
        continue