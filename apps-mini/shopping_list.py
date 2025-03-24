## Grocery list app: Stores items in a list. Adds user inputs as items appended to list. 
## Prompts user to add/remove items. Stores a list of items the store is out of. 
## If users attempts to add an out-of-stock item user is given an alert. 
##
## feature list:
## done -  print list out as numbered line items when > 5 items
## done - turn loop ( list formmatting) into function
## done - turn loop (add user inputs into item) into function 
## user input to remove items from the list. 
## update function to create a list of numbers and run .pop with each line. 


print("\n\n****\tWelcome To The Shopping List App\t****\n")
print("Current Date and Time: ")

list_grc = ["milk","oatmeal","salad"]

#loop determines formatting of printed list 

def format_list_loop(grocery_list): 
    #if list is empty prints: 
    if not grocery_list:
        print("Your grocery list is currently empty. Lets get started!\n") 
    #if list has more than 5 items in it currently prints #. list
    elif len(grocery_list) > 5 :
        print(f"Grocery List: {len(grocery_list)} items")
        for i,item in enumerate(grocery_list, start=1):
            print(f"{i}. {str(item.title())}")     
    #if list has < 5 items prints as "item + and + item"
    else:   
        formatted_list = ' and '.join([item.title() for item in grocery_list])
        print(f"You currently have {len(list_grc)} items: ({formatted_list}) in your list.")


def add_items(grocery_list):
#loop to add user inputs as items. 
    while True:
        ans_add = input("\nWould you like to add more items to this list? ('Yes' or 'No'):\t\n").strip()
        if ans_add[:2] == "no":
            print("\n", end="")
            format_list_loop(grocery_list)
            #print("****\t\t\t\t\t\t****")
            break
        while True:
        # add items to list
            user_item = input("Enter one item at a time to add to the grocery list \n\t--Or type \"Done\" when finished: ").strip().title()
            if user_item == "Done":
                break
            grocery_list.append(user_item)

def numbered_list(grocery_list):
    for i, item in enumerate(grocery_list, start= 1):
        print(f"{i}. {str(item.title())}")

format_list_loop(list_grc)
add_items(list_grc)

'''
while True: 
    try:
        # ask user if they need to remove any items. 
        if_remove = input("Would you like to remove any items from your list? Enter 'Yes' or 'No'").title()
        if if_remove == "yes":
            print("Below is your Shopping List")
            numbered_list(grocery_list)
            #exception handling to catch non numeric values. 
            try:
                #could turn the input of numbers into a list iteself. 
                to_remove = int(input("Enter the number of the item you wish to remove: "))
                xit = (to_remove - 1)
                removed_item = list_grc.pop(xit)
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("Please enter a number of an item in the list. If multiple inputs, comma seperate them eg:(3, 6, 9, ..) "

    except :
        print("Please type \"Yes\" or \"No\"")

'''

print("\n****\t\t\t\t\t\t****\n")