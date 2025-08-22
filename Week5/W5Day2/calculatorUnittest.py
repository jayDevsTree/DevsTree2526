import unittest

class Calculator:
    def add(self, *nums):
        return sum(nums)

    def subtract(self, *nums):
        if not nums:
            return 0
        result = nums[0]
        for n in nums[1:]:
            result -= n
        return result

    def multiply(self, *nums):
        if not nums:
            return 1
        result = 1
        for n in nums:
            result *= n
        return result

    def divide(self, *nums):
        if not nums:
            return None
        result = nums[0]
        for n in nums[1:]:
            if n == 0:
                raise ZeroDivisionError("division by zero")
            result /= n
        return result

    def power(self, base, exponent):
        return base ** exponent
    
    
class TestCalculator(unittest.TestCase):
    def setUp(self):# this is a special hook that work in unittest framework
        self.calc = Calculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(1, 2, 3), 6)
        self.assertEqual(self.calc.add(1, 2, 3, 4), 10)
        
    def test_addition_empty(self):
        self.assertEqual(self.calc.add(), 0)
    
    def test_substraction_empty(self):
        self.assertEqual(self.calc.subtract(), 0)
        
    def test_multiply_empty(self):
        self.assertEqual(self.calc.multiply(), 1)
        
    def test_division_empty(self):
        self.assertEqual(self.calc.divide(), None)
        
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)
            
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(2, 0), 1)
        
if __name__ == '__main__':
    unittest.main()