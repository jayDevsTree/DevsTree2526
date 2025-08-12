class SafeCalculator:
    
    def __init__(self):
        print("This is a Safe Calculator")
        self.result = 0
        
    def checkInput(self, *nums):
        if len(nums) < 2:
            raise notValidInput("Not enough input or invalid Input")
        try:
            [float(num) for num in nums] 
        except ValueError:
            raise notValidInput("Input must be numeric")
    
    def add(self, *nums):
        self.checkInput(*nums)
        self.result = sum(nums)
        return self.result
    
    def substract(self, *nums):
        self.checkInput(*nums)
        return self.safeSubstract(*nums)
    
    def safeSubstract(self, *nums):
        self.checkInput(*nums)
        if len(nums) != 2:
            raise checkOnlyTwoInput("Only two inputs are allowed for subtraction")
        self.result = nums[0] - nums[1]
        return self.result
    
    def multiply(self, *nums):
        self.checkInput(*nums)
        self.result = 1
        for num in nums:
            self.result *= num
        return self.result
    
    def divide(self, *nums):
        self.checkInput(*nums)
        return self.safeDivide(*nums)
    
    def safeDivide(self, *nums):
        self.checkInput(*nums)
        if len(nums) != 2:
            raise checkOnlyTwoInput("Only two inputs are allowed for division")
        if nums[1] == 0:
            raise notValidInput("Division by zero is not allowed")
        self.result = nums[0] / nums[1]
        return self.result


# Custom Exceptions
class notValidInput(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'invalid input: {self.message}'
    
class checkOnlyTwoInput(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'invalid input: {self.message}'


obj1 = SafeCalculator()

try:
    print('Addition of (args):',obj1.add(1, 2, 3, 4, 5))
    print('Subtraction (only Two args):',obj1.substract(1, 2))      # works
    print('Multiplication of (args):',obj1.multiply(1, 2, 3, 4))
    print('Division (only Two args):',obj1.divide(10, 0))        # division by zero error
except (notValidInput, checkOnlyTwoInput) as e:
    print("Caught custom exception:", e)
