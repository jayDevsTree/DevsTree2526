import unittest

class calculator(unittest.TestCase):

    def test_addition(self):
        def add(*nums):
            total = 0
            for num in nums:
                total += num
            return total
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(1,2,3), 6)
        self.assertEqual(add(1,2,3,4), 10)

    def test_substraction(self):
        def substract(*nums):
            if not nums:
                return 0
            result = nums[0]
            for n in nums[1:]:
                result -= n
            return result
        self.assertEqual(substract(1,2), -1)
        self.assertEqual(substract(1,2,3), -4)
        self.assertEqual(substract(1,2,3,4), -8)

    def test_multiply(self):
        def multiply(*nums):
            if not nums:
                return 1
            result = 1
            for n in nums:
                result *= n
            return result
        self.assertEqual(multiply(1,2), 2)
        self.assertEqual(multiply(1,2,3), 6)
        self.assertEqual(multiply(1,2,3,4), 24)
        self.assertEqual(multiply(0), 0)

    def test_division(self):
        def divide(*nums):
            if not nums:
                return None
            result = nums[0]
            for n in nums[1:]:
                result /= n
            return result
        self.assertEqual(divide(1,2), 0.5)
        self.assertEqual(divide(1,2,3), 0.16666666666666666)
        self.assertEqual(divide(1,2,3,4), 0.041666666666666664)
        self.assertEqual(divide(0), 0)

if __name__ == '__main__':
    unittest.main() 