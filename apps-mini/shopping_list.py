## Grocery list app
## feature list:
##done -  print list out as numbered line items when > 5 items


print("\n\n****\tWelcome To The Shopping List App\t****\n")
print("Current Date and Time: ")

list_grc = ["milk","oatmeal","salad","deoderant", "socks"]

while True: 
    if not list_grc:
        print("Your grocery list is currently empty. Lets get started!\n") 
        break
    elif len(list_grc) > 5 :
        print("Grocery List:")
        for i,item in enumerate(list_grc, start=1):
            print(f"{i}. {item.title()}")
        break       
    else:   
        formatted_list = ' and '.join([item.title() for item in list_grc])
        print(f"You currently have: ({formatted_list}) in your list.")
        break

input("Would you like to add to this list?:\t").strip()
