import unittest
import string_utils


class testStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string('hello'), 'olleh')
        
    def test_is_palindrome(self):
        self.assertTrue(string_utils.string_palindrome('racecar'))
        self.assertFalse(string_utils.string_palindrome('hello'))
        
    def test_count_vowels(self):
        self.assertEqual(string_utils.count_vowels('hello'), 2)
        self.assertEqual(string_utils.count_vowels('racecar'), 3)
        
    def test_count_consonants(self):
        self.assertEqual(string_utils.count_consonants('hello'), 3)
        self.assertEqual(string_utils.count_consonants('racecar'), 4)
        
    def  test_reverse_empty_string(self):
        self.assertEqual(string_utils.reverse_string(''), '')
        
    def test_count_empty_string(self):
        self.assertEqual(string_utils.count_vowels(''), 0)
        self.assertEqual(string_utils.count_consonants(''), 0)
        
    
    def test_empty_numbers(self):
        self.assertEqual(string_utils.num_palindrome(''), 'Not a Number')
    def  test_number_palindrome(self):
        self.assertEqual(string_utils.num_palindrome(12321), True)
        self.assertEqual(string_utils.num_palindrome(1231), False) 
        
        
if __name__ == '__main__':
    unittest.main()  
    
    
