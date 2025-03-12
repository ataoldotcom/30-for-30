##Multiplication/Exponent Table app
##need to change the code so that its storing results in a list. 
## fix the print station in the function if itend to RETURN results

print("Welcome to the Multiplication/Exponent Table App")

name = input("What is your name:\t").strip().title()


def table_m(numb):
    for i in range (1,10):
        print(f"\t {i} * {user_number} = {round(i * numb, 2)}")
        #return round(i * numb, 2)


while True:


    try:
        user_number = float(input("What number would you like to work with?:\t"))
        k = table_m(user_number)
        print(f"\nMultiplication Table for {user_number}\n")
        #print(k)
        #need to add print statements for math equations
        # or create a cascading function x==0 (x =+ 1,9)  * number
        break
    except ValueError:
        print("Enter a numberic value only.")