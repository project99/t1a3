
def print_list_of_items(items):
    for item in items:
        print(item)

# adds a new item to the menu
def add_item(oga_items, add_name, add_price):

    new_item = {"name": add_name, "price": add_price}
    oga_items.append(new_item)

def delete_item(ogd_items, del_name):
    # iterate through the list looking for the item
    for lu_item in ogd_items:
        # check if the item's name of this iteration is equal to the name we receive.
        if lu_item["name"] == del_name:
            # access to the list and remove the item
            ogd_items.remove(lu_item)
            print(f"{del_name} was removed from the menu")

        print("")   

def update_item_price(items, name):
    # iterate through the list looking for the item
    for item in items:
        # check if the item's name of this iteration is equal to the name we receive.
        if item["name"] == name:
            # ask for the new price
            new_med = input("What would you like to add: ")
            #update the item's price
            item["character"].extend(new_med)
            print(f"{new_med} was addeded")

        print(f"{name} is not in the menu")   
