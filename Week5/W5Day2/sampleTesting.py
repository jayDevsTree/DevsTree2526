import unittest

def add(*nums):
    total= 0
    for num in nums:
        total += num
    return total

def subtract(*nums):
    total= 0
    for num in nums:
        total -= num
        
    return total

class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1,2,3),6)
        
    def test_subtract(self):
        self.assertEqual(subtract(1,2,3),-6)
        
        
if __name__ == '__main__':
    unittest.main()