def reverse_string(s):
    return s[::-1]

def string_palindrome(s):
    str = ''
    for ch in s:
        if ch != ' ':
            str = ch + str
    rev_str = ''
    for ch in range(len(str)-1,-1,-1):
        rev_str = rev_str + str[ch]
        
    return True if str == rev_str else False

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in ['a','e','i','o','u']:
            count += 1
    return count

def count_consonants(s):
    count = 0
    for ch in s:
        if ch not in ['a','e','i','o','u']:
            count += 1
    return count


def num_palindrome(num):
    try:
       int(num)
    except ValueError:
        return 'Not a Number'
    
    # return s == s[::-1]
    origin_num = num
    rev_num = 0
    while(num != 0):
        last_digit = num % 10
        rev_num = rev_num * 10 + last_digit
        num = num // 10
    return True if rev_num == origin_num else False
        
    

    