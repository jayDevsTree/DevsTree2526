def oneWay():
    
    def decor(printer):
        def inner():
            printer() # existing code
            print("This is a Third Line")
            
        return inner


    def printer():
        print("This is a First line")
        print("This is a Second line")
        

    printer = decor(printer)
    printer()


def SecondWay():
    
    def decor(printer):
        def inner():
            printer() # this is a existing code
            print("Hello 3")    
        return inner
    
    @decor # --> printer = decor(printer)
    def printer():
        print("Hello 1")
        print("Hello 2")
        
    printer()

oneWay()
print("--------")
SecondWay()



