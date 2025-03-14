## Grade Sorter app
# add range validation to input

print("\n\n*****\tWelcome to the grade sorter app\t*****\n")

while True:
    try:
        #need to fix. currently the loop reverts to begining when you enter a non-int
        #possibly add i loop with exception handling instead. 
        grade_1 = int(input("\tWhat is your first  grade (0-100): "))
        grade_2 = int(input("\tWhat is your second grade (0-100): "))
        grade_3 = int(input("\tWhat is your third  grade (0-100): "))
        grade_4 = int(input("\tWhat is your fourth grade (0-100): "))
        grade_5 = int(input("\tWhat is your fifth  grade (0-100): "))
        break
    except ValueError:
        print("Please enter a whole integer grade")
        continue

user_grades = [grade_1, grade_2, grade_3, grade_4, grade_5]
 
user_grades.sort(reverse=True)
 
high = sorted(user_grades, reverse=True)[0]


print(f"\nYour grades highest to lowest are: {user_grades}\n")
print("The lowest two grades will now be dropped")
low_1 = user_grades.pop(-1)
low_2 = user_grades.pop(-1)
print(low_1)
print(low_2)
print(f"\nYour remaining grades are: {user_grades}")
print(f"Nice work! Your highest grade is a {high}\n\n")

