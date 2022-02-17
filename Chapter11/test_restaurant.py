#Russell Arlt
#Hands on #2

from restaurant import Restaurant
import unittest

class testRest(unittest.TestCase):
    def setUp(self):
        restaurant_name = "Dales Grillers"
        cuisine_type = "American Fare"
        self.restaurant = Restaurant(restaurant_name, cuisine_type)

    def test_set_number_served(self):
        custos = 10000
        self.restaurant.set_number_served(custos)
        self.assertEqual(self.restaurant.number_served, 10000)
        
    def test_increment_number_served(self):
        increase = 58
        self.restaurant.increment_number_served(increase)
        self.assertEqual(self.restaurant.number_served, 10058)
       

if __name__ == "__main__":
    unittest.main()