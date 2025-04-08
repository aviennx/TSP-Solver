import random
import numpy as np
from .utils import Route, City

class Ant:
    def __init__(self, start_city, cities):
        self.start_city = start_city
        self.cities = cities
        self.visited = [start_city]
        self.current_city = start_city
        self.distance = 0
    
    def choose_next_city(self, pheromones, alpha=1, beta=2):
        unvisited = [city for city in self.cities if city not in self.visited]
        if not unvisited:
            return None
            
        probabilities = []
        total = 0
        
        for city in unvisited:
            pheromone = pheromones[self.cities.index(self.current_city)][self.cities.index(city)]
            distance = self.current_city.distance(city)
            probability = (pheromone ** alpha) * ((1/distance) ** beta)
            probabilities.append(probability)
            total += probability
            
        probabilities = [p/total for p in probabilities]
        return random.choices(unvisited, weights=probabilities)[0]
    
    def move(self, pheromones):
        next_city = self.choose_next_city(pheromones)
        if next_city:
            self.distance += self.current_city.distance(next_city)
            self.current_city = next_city
            self.visited.append(next_city)
            return True
        return False

class ACO:
    def __init__(self, cities, num_ants=50, max_iter=100, alpha=1, beta=2, rho=0.5, q=100):
        self.cities = cities
        self.num_ants = num_ants
        self.max_iter = max_iter
        self.alpha = alpha
        self.beta = beta
        self.rho = rho  # evaporation rate
        self.q = q  # pheromone constant
        self.pheromones = np.ones((len(cities), len(cities)))
        
    def update_pheromones(self, ants):
        # Evaporate pheromones
        self.pheromones *= (1 - self.rho)
        
        # Add new pheromones
        for ant in ants:
            for i in range(len(ant.visited)-1):
                current_idx = self.cities.index(ant.visited[i])
                next_idx = self.cities.index(ant.visited[i+1])
                self.pheromones[current_idx][next_idx] += self.q / ant.distance
                self.pheromones[next_idx][current_idx] = self.pheromones[current_idx][next_idx]
    
    def run(self):
        best_route = None
        best_distance = float('inf')
        progress = []
        
        for _ in range(self.max_iter):
            ants = [Ant(random.choice(self.cities), self.cities) for _ in range(self.num_ants)]
            
            # Move all ants
            for ant in ants:
                while ant.move(self.pheromones):
                    pass
                
                # Complete the tour
                ant.distance += ant.current_city.distance(ant.start_city)
                ant.visited.append(ant.start_city)
                
                if ant.distance < best_distance:
                    best_distance = ant.distance
                    best_route = Route(ant.visited)
            
            self.update_pheromones(ants)
            progress.append(best_distance)
            
        return best_route, progress
