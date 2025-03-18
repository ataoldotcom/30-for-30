## Grocery list app: Stores items in a list. Adds user inputs as items appended to list. 
## Prompts user to add/remove items. Stores a list of items the store is out of. 
## If users attempts to add an out-of-stock item user is given an alert. 
##
## feature list:
##done -  print list out as numbered line items when > 5 items
## turn loop ( list formmatting) into function
## turn loo (add user inputs into item) into function 


print("\n\n****\tWelcome To The Shopping List App\t****\n")
print("Current Date and Time: ")

list_grc = ["milk","oatmeal","salad","deoderant", "socks"]

#loop determines formatting of printed list 
while True: 
    #if list is empty prints: 
    if not list_grc:
        print("Your grocery list is currently empty. Lets get started!\n") 
        break
    #if list has more than 5 items in it currently prints #. list
    elif len(list_grc) > 5 :
        print("Grocery List:")
        for i,item in enumerate(list_grc, start=1):
            print(f"{i}. {str(item.title())}")
        break       
    #if list has < 5 items prints as "item + and + item"
    else:   
        formatted_list = ' and '.join([item.title() for item in list_grc])
        print(f"You currently have: ({formatted_list}) in your list.")
        break

#loop to add user inputs as items. 
while True:
    ans_add = input("Would you like to add more items to this list? ('Yes' or 'No'):\t").strip()
    if ans_add[:2] == "no":
        break
    while True:
    # add items to list
        user_item = input("\nEnter one item at a time to add to the grocery list \n\t--Or type \"Done\" when finished: ").strip().title()
        if user_item == "Done":
            break
        list_grc.append(user_item)

print(list_grc)