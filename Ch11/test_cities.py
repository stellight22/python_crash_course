#11-1 test city_country
import unittest
from city_country import city_country

class placesTestCase(unittest.TestCase):
    # tests for test_cities.py

    def test_city_country(self):
        city_plus_country = city_country('Johannesberg', 'South Africa')
        self.assertEqual(city_plus_country, {'city': 'Johannesberg', 'country': 'South Africa'})

unittest.main()