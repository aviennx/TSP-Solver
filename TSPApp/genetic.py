import numpy as np
from .utils import Route

class GeneticAlgorithm:
    def __init__(self, cities, population_size=100, elite_size=20, mutation_rate=0.01):
        self.cities = cities
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate
        self.population = []
        
        # Precompute distance matrix for faster calculations
        self.distance_matrix = np.zeros((len(cities), len(cities)))
        for i in range(len(cities)):
            for j in range(len(cities)):
                self.distance_matrix[i][j] = cities[i].distance(cities[j])
    
    def create_initial_population(self):
        for _ in range(self.population_size):
            route = self.cities.copy()
            np.random.shuffle(route)
            self.population.append(Route(route))
    
    def rank_routes(self):
        return sorted(self.population, key=lambda x: x.distance)
    
    def selection(self, ranked_population):
        selection_results = []
        for i in range(self.elite_size):
            selection_results.append(ranked_population[i])
        
        for i in range(len(ranked_population) - self.elite_size):
            selection_results.append(self.tournament_selection(ranked_population))
        return selection_results
    
    def tournament_selection(self, ranked_population):
        tournament = []
        for _ in range(5):
            tournament.append(np.random.choice(ranked_population))
        return min(tournament, key=lambda x: x.distance)
    
    def breed(self, parent1, parent2):
        child = []
        geneA = np.random.randint(0, len(parent1.cities))
        geneB = np.random.randint(0, len(parent1.cities))
        
        start_gene = min(geneA, geneB)
        end_gene = max(geneA, geneB)
        
        for i in range(start_gene, end_gene):
            child.append(parent1.cities[i])
            
        for city in parent2.cities:
            if city not in child:
                child.append(city)
                
        return Route(child)
    
    def breed_population(self, selection_results):
        children = []
        length = len(selection_results) - self.elite_size
        pool = np.random.choice(selection_results, len(selection_results), replace=False)
        
        for i in range(self.elite_size):
            children.append(selection_results[i])
            
        for i in range(length):
            child = self.breed(pool[i], pool[len(selection_results)-i-1])
            children.append(child)
        return children
    
    def mutate(self, individual):
        for swapped in range(len(individual.cities)):
            if np.random.random() < self.mutation_rate:
                swap_with = np.random.randint(0, len(individual.cities)-1)
                individual.cities[swapped], individual.cities[swap_with] = individual.cities[swap_with], individual.cities[swapped]
        return individual
    
    def next_generation(self):
        ranked_population = self.rank_routes()
        selection_results = self.selection(ranked_population)
        children = self.breed_population(selection_results)
        next_generation = []
        for individual in children:
            next_generation.append(self.mutate(individual))
        self.population = next_generation
    
    def run(self, generations=500):
        self.create_initial_population()
        progress = []
        
        for i in range(generations):
            self.next_generation()
            progress.append(self.rank_routes()[0].distance)
            
        return self.rank_routes()[0], progress
