shop_list=[]
    
def shopping_list():
    item_num= int(input('Enter how many items you want to add: '))

    for i in range(item_num):
        item = input(f'Enter {i+1}th item name: ')
        shop_list.append(item)
        
    is_remove = input('Do you want to remove any item(0/1): ')
    if is_remove=='1':
        remove_CartItems()
    else:
        print(f"Shopping cart:{shop_list}")

def remove_CartItems():
    remove_item = input('Enter the item you want to remove: ')
    if remove_item not in shop_list:
        print('Item not found ')
    else:
    # shop_list.remove(remove_item)
        # removeAfter_list = [item for item in shop_list if item != remove_item]
        # print(f"Shopping cart:{removeAfter_list}")
        
        shop_list[:] = [item for item in shop_list if item != remove_item]#memory efficient change in global list not make copy or local list
        print(f"Shopping cart:{shop_list}")
        
shopping_list()

