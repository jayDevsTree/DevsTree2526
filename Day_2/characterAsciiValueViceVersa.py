char = input("Enter a Single character: ")
if len(char) == 1:
    ascii_value = ord(char)
    print(f"ASCII value '{char}' is {ascii_value}")
else:
    print("Invalid Input")


ascii_code = int(input("Enter an ASCII code(0-127): "))
try:
    char = chr(ascii_code)
except:
    print("Invalid ASCII code")
print(f"ASCII code {ascii_code} is '{char}'")