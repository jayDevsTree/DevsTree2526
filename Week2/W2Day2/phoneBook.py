def phoneBook():
    phoneBook = {}
    count = int(input("Enter how many contacts you want to add:"))
    while (count >= 1):
        name = input("Enter your Name:")
        number = input("Enter your Number:")
        phoneBook[name.lower()] = number
        count -= 1

    print(phoneBook)
    
    print("If you want to search any Contact?,(1/0)")
    search = int(input())
    
    
        
    if search == 1: 
        print('''can you know name or number?
          if you know name press '0'
          if you know number press '1' ''')
    
    known = int(input())
    #names
    if known == 0:
        searchName = input("Enter name to search:").lower()
        if searchName in phoneBook:#phoneBook.keys()
            print(phoneBook[searchName])
        else:
            print("Not Found")
    if known == 1:
        #numbers
        number = input("Enter number to search:")
        # for name in phoneBook:
        #     if phoneBook[name] == number:
        #         print(name)
        #         break
        # else:
        #     print("Not Found")
        
        
        # first we need to convert dict to list and then list(dict.keys())and that key for we need value of index number for that we need list(dict.keys())[list(dict.values()).index(number)]
        if number in phoneBook.values():
           temp =  list(phoneBook.keys())
        #    print(temp)
           temp_val = list(phoneBook.values())
           print(temp[temp_val.index(number)])
           
           
        #    print(temp[list(phoneBook.values()).index(number)])
            # print(list(phoneBook.keys())[list(phoneBook.values()).index(number)])
        else:
            print("Not Found")
       
    else:
        print("Thank You!")
        
        
        
phoneBook()