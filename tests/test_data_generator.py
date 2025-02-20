import unittest
from data_generator.generator import get_random_list

class TestDataGenerator(unittest.TestCase):

    def test_get_random_list_length(self):
        """Test if the generated list has the correct length."""
        size = 10
        result = get_random_list(size)
        self.assertEqual(len(result), size, "The list length does not match the expected size.")

    def test_get_random_list_values(self):
        """Test if the generated list values are within the specified limit."""
        size = 10
        limit = 100
        result = get_random_list(size, limit)
        for value in result:
            self.assertGreaterEqual(value, 0, "List contains values less than 0.")
            self.assertLessEqual(value, limit, f"List contains values greater than {limit}.")

if __name__ == '__main__':
    unittest.main()
