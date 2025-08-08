import io
import sys

filePath = 'Week4/W4Day1/textFileProcessor.txt'


def read_file():
    with open(filePath,'r') as f:
        print(f.read())
# read_file()

def newText_file():
    with open (filePath,'w') as f:
        text = input("Enter Text: ")
        f.write(text)
        read_file()
# newText_file()
        
def addText_file():
    with open(filePath,'a+') as f:
        text = input("Enter Text: ")
        f.write("\n")
        f.write(text)
        read_file()
        # f.seek(0)
        # print(f.read())
# addText_file()

def count_lines():
    with open(filePath, 'r')as f:
        lines = f.readlines()
        print(lines)
        print(f'Total lines in File: {len(lines)}')
        
        #second way because this should readlines() pointer go end then reStart from f.seek(0)
        # print()
        # f.seek(0)
        # print(f.readlines())
        # f.seek(0)
        # print(f'Total lines in File: {len(f.readlines())}')
        
        #third way to manually count lines
        # line_count = 0
        # for line in f:
        #     if line != '\n':
        #         line_count += 1
        # lines = f.readlines()
        # print(lines)
        # print(f'Total lines in File: {line_count}')


def count_words_in_file():
    with open(filePath, 'r') as f:
        file_whole_text = f.read()
        words_in_file = file_whole_text.split()
        # print(words_in_file)
        print(f'Total words in File: {len(words_in_file)}')

def count_word_in_line():
    with open (filePath, 'r') as f:
        total_lines = f.readlines()
        for index,each_line in enumerate(total_lines, start=1):
            word_in_line = each_line.split()
            # print(word_in_line)
            print(f'Total words in {index}th Line : {len(word_in_line)}')
        
        
def count_char_in_file():
    # with open(filePath, 'r') as f:
    with open (filePath, 'r') as f:
        
        # first way good
        # file_whole_text = f.read()
        # char_in_file = len(file_whole_text)
        # print(f'Total char in File: {char_in_file}')
        
        #manual way to count
        file_whole_text = f.read()
        characters_in_file = [char for char in file_whole_text]
        print(f'Total char in File: {len(characters_in_file)}')
        print()
        
        # second way for list understanding
        # characters_in_file = list(file_whole_text)
        # print(characters_in_file)
        # print(f'Total char in File: {len(characters_in_file)}')
        

def count_char_in_line():
    with open (filePath, 'r') as f:
        total_lines = f.readlines()
        for index,each_line in enumerate(total_lines, start=1):
            char_in_line = [char for char in each_line]
            print(f'Total char in {index}th Line : {len(char_in_line)}')
            
            
# count_words_in_file()
# print()
# count_word_in_line()
# print()
# count_char_in_file()
# print()
# count_char_in_line()

def store_result():
    # Save the original stdout
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout  
    
    count_words_in_file()
    print()
    count_word_in_line()
    print()
    count_char_in_file()
    print()
    count_char_in_line()
    
    # Restore stdout
    sys.stdout = old_stdout
    
    # Get captured output
    result_text =  new_stdout.getvalue()
    
    # Save to file
    with open('Week4/W4Day1/Result_textFileProcessor.txt', 'w') as f:
        f.write(result_text)

store_result()
