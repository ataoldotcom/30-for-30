## Grade Sorter app



while True:
    try:
        #need to fix. currently the loop reverts to begining when you enter a non-int
        #possibly add i loop with exception handling instead. 
        grade_1 = int(input("What is your first  grade (0-100)"))
        grade_2 = int(input("What is your second grade (0-100)"))
        grade_3 = int(input("What is your third  grade (0-100)"))
        grade_4 = int(input("What is your fourth grade (0-100)"))
        grade_5 = int(input("What is your fifth  grade (0-100)"))
        break
    except ValueError:
        print("Please enter a whole integer grade")
        continue

user_grades = [grade_1, grade_2, grade_3, grade_4, grade_5]
#need to add sorting to original list. although not the best practice. 
user_grades.sort(reverse=True)
#type error. can not sort integers. 
high = sorted(user_grades, reverse=True)[0]


print(user_grades)
input()
print(high)
input()

print(f"\nYour grades highest to lowest are: {high}\n")
print("The lowest two grades will now be dropped")
low_1 = user_grades.pop(-1)
low_2 = user_grades.pop(-1)
print(low_1)
print(low_2)
print(f"\nYour remaining grades are: {user_grades}")
print(f"Nice work! Your highest grade is a {high}")

