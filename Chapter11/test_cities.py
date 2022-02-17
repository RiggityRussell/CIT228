import unittest
from city_functions import cityCountry

class test(unittest.TestCase):
    def test_city_country(self):
        result = cityCountry("berlin", "germany")
        result2 = cityCountry("lincoln", "nebraska", "20,000")
        self.assertEqual(result, "Germany, Berlin")
        self.assertEqual(result2, "Nebraska, Lincoln, Population: 20,000")

if __name__ == '__main__':
    unittest.main()

