#11-1 test city_country
import unittest
from city_country import get_data_city

class placesTestCase(unittest.TestCase):
    # tests for test_cities.py

    def test_city_country(self):
        my_city = get_data_city('johannesberg', 'South Africa')
        self.assertEqual(my_city, 'Johannesberg, South Africa')

    def test_population(self):
        my_city_2 = get_data_city('venice', 'italy', population = 261905 )
        self.assertEqual(my_city_2, 'Venice, Italy, population: 261905')


unittest.main()