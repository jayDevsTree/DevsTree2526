with open("C:/Users/jaykp/Desktop/Devstree Task/Week3/sample.txt", "r") as f:
    text = f.read()
print(text)


with open("pythontxt1.txt", 'w') as file:
    file.write("This is a Python file that writing Mode test")

with open("pythontxt1.txt", "r") as f:
    text = f.read()

print(text)

if "python" in text.lower():
    print("Text is present ")
else:
    print("Text is not present ")
