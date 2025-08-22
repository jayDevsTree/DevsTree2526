import pdb

# n → go to next lin
# s → step inside function
# p num → print current value of num
# p total → print running total
# c → continue execution

def calculate_average(numbers):
    total = 0
    count = len(numbers)

    for num in numbers:
        pdb.set_trace()  # Debugging will pause here
        total += num

    average = total / count
    return average

def main():
    nums = [10, 20, 30, 0] 
    result = calculate_average(nums)
    print("Average is:", result)

if __name__ == "__main__":
    main()
