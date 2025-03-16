## Grocerly list app
## feature list:
## print list out as numbered line items when > 5 items


print("\n\n****\tWelcome To The Shopping List App\t****\n")
print("Current Date and Time: ")

list_grc = ["milk","oatmeal","salad","deoderant", "socks", "potatoes"]

while True: 
    if not list_grc:
        print("Your grocery list is currently empty. Lets get started!\n") 
        break
    elif len(list_grc) > 5 :
       #print("checking loop seq is working")
       #need print numbered list
        for i in range(len(list_grc)):
            print('i. '.join([item.title() for item in list_grc]))
            break       
    else:   
        print(f"You currently have: ({' and '.join([item.title() for item in list_grc])}) in your list.\n")
        break

