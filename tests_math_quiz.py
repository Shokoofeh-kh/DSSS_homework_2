import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result

class TestMathGame(unittest.TestCase):

  def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

   def test_generate_random_operator(self):
        # Test if the result of generate_random_operator is one of the expected operators
        operators = {'+', '-', '*'}
        result = generate_random_operator()
        self.assertIn(result, operators)

   def test_calculate_result(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '*', '10 * 3', 30),
            (8, 4, '-', '8 - 4', 4),
            # Add more test cases as needed
        ]

if __name__ == "__main__":
    unittest.main()
