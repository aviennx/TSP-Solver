import unittest
from TSPApp.utils import City, Route
from TSPApp.data_loader import generate_random_cities

class TestTSP(unittest.TestCase):
    def setUp(self):
        self.cities = [City(0, 0), City(1, 0), City(0, 1), City(1, 1)]
    
    def test_city_distance(self):
        self.assertAlmostEqual(self.cities[0].distance(self.cities[1]), 1.0)
        self.assertAlmostEqual(self.cities[0].distance(self.cities[2]), 1.0)
    
    def test_route_distance(self):
        route = Route(self.cities)
        self.assertAlmostEqual(route.distance, 4.0)
    
    def test_random_cities(self):
        cities = generate_random_cities(10)
        self.assertEqual(len(cities), 10)
        self.assertTrue(all(isinstance(city, City) for city in cities))

if __name__ == '__main__':
    unittest.main()
