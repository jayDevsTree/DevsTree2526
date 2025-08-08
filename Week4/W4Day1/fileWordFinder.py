# Program to find word in a file
    
with open('Week4/W4Day1/wordFind.txt', 'r') as f:
    target = input("Enter Word to find: ").lower()
    text = f.read()
    f.seek(0)

    print("Approach 1: Using enumerate() way")
    for i, line in enumerate(f, start=1):
        if target in line.lower():
            print(f"Target={target} on lineno {i},")
            print(f'line:{line.strip()}')
            break
    else:
        print("Not Found")
    print()
    f.seek(0)
    print("Approach 2: Using for loop and text.split('\\n')")
    for i, line in enumerate(text.split('\n'), start=1):
        if target in line.lower():
            print(f'Target: {target} found in line {i}')
            print(line)
            break
    else:
        print("Not Found!")

    f.seek(0)
    print()
    print("Approach 3: Using readlines()")
    lines = f.readlines()
    isWord_notin_Line = True
    for i, line in enumerate(lines, start=1):
        if target in line.lower():
            print(f'Target: {target} found in line {i}')
            print(line.strip())
            isWord_notin_Line = False
            break
    if isWord_notin_Line:
        print("Not Found!")
    print()
    f.seek(0)
    print("Approach 4: Convert all lines to lowercase in memory")
    lines = f.readlines()
    lines_lower = [line.lower() for line in lines]
    found = False
    for i, line in enumerate(lines_lower, start=1):
        if target in line:
            print(f"Target: {target} found in line {i}")
            print(lines[i-1].strip())
            found = True
            break
    if not found:
        print("Not Found!")

    f.seek(0)
    print()
    
    print("Approach 5: Using each word in file line method")
    
    each_word_line = []
    
    line_no = 0
    for line in f:
        line_no += 1
        line_word = line.strip().split(' ')
        for word in line_word:
            each_word_line.append(word.lower())
        if target.lower() in each_word_line:
            print(f"Target = {target} on line {line_no}")
            print(line.strip())
            break
    else:
        print("Not Found!")

    