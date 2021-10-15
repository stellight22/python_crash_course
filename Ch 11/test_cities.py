import unittest
from city_functions import city_country

class City_Test(unittest.TestCase):

    def test_city_function(self):
        city_return_val = city_country('cancun', 'mexico')
        self.assertEqual(city_return_val, 'Cancun, Mexico')

    def test_population(self):
        population_return = city_country('cancun', 'mexico', '500000')
        self.assertEqual(population_return, 'Cancun, Mexico population: 500000')

unittest.main()