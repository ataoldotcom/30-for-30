##Multiplication/Exponent Table app
##need to change the code so that its storing results in a list. 
## fix the print station in the function if itend to RETURN results

print("***\tWelcome to the Multiplication/Exponent Table App\t***\n")

name = input("\nWhat is your name:\t").strip().title()


def table_m(numb):
    #can not append on a float
    results = []
    for i in range (1,12):
        sol = round(i * numb, 2) 
        #appending on list instead of sol. 
        results.append(f"\t {f'{i} * {user_number}':<10}= {sol}")    
    #return sol
    return "\n".join(results)

def table_ex(numb):
    results_e = []
    for i in range (1,12):
        sol_e = round(numb ** i,2)
        results_e.append(f"\t {f'{user_number} ** {i}':<10}= {sol_e}")
    return "\n".join(results_e)

while True:


    try:
        user_number = float(input("\nWhat number would you like to work with?:\t"))
        chart_m = table_m(user_number)
        chart_ex = table_ex(user_number)
        print(f"\nMultiplication Table for {user_number}\n")
        print(chart_m)
        print(f"\nExponent Table for {user_number}\n")
        print(chart_ex)
        #need to add print statements for math equations
        # or create a cascading function x==0 (x =+ 1,9)  * number
        break
    except ValueError:
        print("Enter a numberic value only.")

print(f"\n****\tMath application complete, {name}!\t****\n")