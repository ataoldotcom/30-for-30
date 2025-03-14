## Grocerly list app
## feature list:
## 1 print list out as numbered line items when > 5 items


print("\n\n****\tWelcome To The Shopping List App\t****\n")
print("Current Date and Time: ")

list_grc = ["milk","oatmeal","salad","deoderant"]

while True: 
    if not list_grc:
        print("Your grocery list is currently empty. Lets get started!\n") 
        break
    # possibly add elif #rd items
    else:   
        print(f"You currently have: ({' and '.join([item.title() for item in list_grc])}) in your list.\n")
        break

