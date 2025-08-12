print("Welcome to File Operations using Exceptions,")

# Custom Exception
class filePermissionsChecker(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"[Permission Error]: {self.message}"

class filePermissionException:
    @staticmethod
    def readFilePermissionException():
        return filePermissionsChecker("You have no permission to read file")
    @staticmethod
    def writeFilePermissionException():
        return filePermissionsChecker("You have no permission to write file")  
    @staticmethod
    def appendFilePermissionException():
        return filePermissionsChecker("You have no permission to append file")

# File Operations 
def readFile_exception(mode):
    allowedModes = ('r','r+','w+','a+')
    if mode not in allowedModes:
        raise filePermissionException.readFilePermissionException()
    with open('Week4/W4Day2/fileOperationWithExceptions.txt','r') as f:
        print('Reading File ...')
        print(f.read())
   
def writeFile_exception(mode):
    allowed_modes = ('w','w+','r+')
    if mode not in allowed_modes: 
        raise filePermissionException.writeFilePermissionException()
    with open('Week4/W4Day2/fileOperationWithExceptions.txt','w') as f:
        newContent_text = input("Enter Text: ")
        f.write(newContent_text)
        print("File Write Successfully!")
        
def appendFile_exception(mode):
    allowed_modes = ('a','a+','r+')
    if mode not in allowed_modes:
        raise filePermissionException.appendFilePermissionException()
    with open('Week4/W4Day2/fileOperationWithExceptions.txt','a') as f:
        text = input("Enter Text: ")
        f.write('\n' + text)
        print("File Append Successfully!")

# Menu
def fileOperation():
    mode_map = {
        1: 'r',
        2: 'w',
        3: 'a',
        4: 'r+',
        5: 'w+',
        6: 'a+'
    }
    
    print('''1 --> r
2 --> w
3 --> a
4 --> r+
5 --> w+
6 --> a+
(any other key to exit)
''')

    try:
        mode_choice = int(input("Enter File Mode: "))
        mode = mode_map[mode_choice]
        if not mode:
            print("Exiting...")
            return
    except ValueError:
        print("Exiting...")
        return
        
    print("Now choose File Operation,")
    print("1 --> Read File")
    print("2 --> Write File")
    print("3 --> Append File")

    try:
        choice = int(input("Enter Choice:"))
    except ValueError:
        print("Invalid Value")
        return
        
    try:
        if choice == 1:
            readFile_exception(mode)
        elif choice == 2:
            writeFile_exception(mode)
        elif choice == 3:
            appendFile_exception(mode)
        else:
            print("Thank You!, Exiting...")
    except filePermissionsChecker as e:
        print('Custom Exception -->', e)
    except FileNotFoundError as f:
        print("File Not Found (builtin) -->", f)
    except PermissionError as p:
        print("PermissionError (builtin) -->", p)
    except Exception as e:
        print("Exception (builtin) -->", e)

fileOperation()
