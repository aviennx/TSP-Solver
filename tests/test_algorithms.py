import unittest
import numpy as np
from TSPApp.data_loader import generate_random_cities
from TSPApp.genetic import GeneticAlgorithm
from TSPApp.pso import PSO
from TSPApp.antcolony import ACO
from TSPApp.utils import Route

class TestTSPAlgorithms(unittest.TestCase):
    def setUp(self):
        # Generate a small set of cities for testing
        self.cities = generate_random_cities(5)
        
    def test_genetic_algorithm(self):
        """Test that genetic algorithm produces valid routes."""
        ga = GeneticAlgorithm(self.cities, population_size=10, elite_size=2)
        ga.create_initial_population()
        
        # Test initial population
        self.assertEqual(len(ga.population), 10)
        for route in ga.population:
            self.assertEqual(len(route.cities), 5)
            self.assertEqual(len(set(route.cities)), 5)  # All cities unique
        
        # Test one generation
        best_route, _ = ga.run(generations=1)
        self.assertIsInstance(best_route, Route)
        self.assertEqual(len(best_route.cities), 5)
        
    def test_pso(self):
        """Test that PSO produces valid routes."""
        pso = PSO(self.cities, num_particles=5)
        best_route, _ = pso.run(iterations=1)
        
        self.assertIsInstance(best_route, Route)
        self.assertEqual(len(best_route.cities), 5)
        self.assertEqual(len(set(best_route.cities)), 5)
        
    def test_aco(self):
        """Test that ACO produces valid routes."""
        aco = ACO(self.cities, num_ants=5)
        best_route, _ = aco.run(iterations=1)
        
        self.assertIsInstance(best_route, Route)
        self.assertEqual(len(best_route.cities), 5)
        self.assertEqual(len(set(best_route.cities)), 5)
        
    def test_route_distance(self):
        """Test route distance calculation."""
        route = Route(self.cities)
        distance = route.distance
        
        # Distance should be positive
        self.assertGreater(distance, 0)
        
        # Distance should be the same regardless of starting point
        rotated_cities = self.cities[1:] + [self.cities[0]]
        rotated_route = Route(rotated_cities)
        self.assertAlmostEqual(distance, rotated_route.distance)

if __name__ == '__main__':
    unittest.main()
