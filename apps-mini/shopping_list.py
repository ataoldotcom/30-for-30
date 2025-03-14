
print("\n\n****\tWelcome To The Shopping List App\t****\n")
print("Current Date and Time: ")

list_grc = ["milk","oatmeal","salad","deoderant"]

while True: 
    if not list_grc:
        print("Your grocery list is currently empty. Lets get started!\n") 
        break
    else:   
        print(f"You currently have {'and'.join(list_grc.title())} in your list.\n")
        break

