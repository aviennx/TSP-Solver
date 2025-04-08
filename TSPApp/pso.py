import random
import numpy as np
from .utils import Route

class Particle:
    def __init__(self, cities):
        self.position = cities.copy()
        random.shuffle(self.position)
        self.velocity = np.zeros(len(cities))
        self.best_position = self.position.copy()
        self.best_distance = float('inf')
        self.update_best()
    
    def update_best(self):
        current_distance = Route(self.position).distance
        if current_distance < self.best_distance:
            self.best_position = self.position.copy()
            self.best_distance = current_distance

class PSO:
    def __init__(self, cities, num_particles=100, max_iter=500, w=0.7, c1=1.5, c2=1.5):
        self.cities = cities
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.w = w  # inertia weight
        self.c1 = c1  # cognitive weight
        self.c2 = c2  # social weight
        self.particles = []
        self.global_best_position = None
        self.global_best_distance = float('inf')
        
    def initialize_particles(self):
        self.particles = [Particle(self.cities) for _ in range(self.num_particles)]
        for particle in self.particles:
            if particle.best_distance < self.global_best_distance:
                self.global_best_position = particle.best_position.copy()
                self.global_best_distance = particle.best_distance
    
    def update_velocity(self, particle):
        for i in range(len(particle.velocity)):
            r1, r2 = random.random(), random.random()
            cognitive = self.c1 * r1 * (particle.best_position[i] - particle.position[i])
            social = self.c2 * r2 * (self.global_best_position[i] - particle.position[i])
            particle.velocity[i] = self.w * particle.velocity[i] + cognitive + social
    
    def update_position(self, particle):
        # Convert velocity to swap probabilities
        swap_probs = 1 / (1 + np.exp(-particle.velocity))
        
        # Perform swaps based on probabilities
        for i in range(len(swap_probs)):
            if random.random() < swap_probs[i]:
                j = random.randint(0, len(particle.position)-1)
                particle.position[i], particle.position[j] = particle.position[j], particle.position[i]
        
        particle.update_best()
        
        if particle.best_distance < self.global_best_distance:
            self.global_best_position = particle.best_position.copy()
            self.global_best_distance = particle.best_distance
    
    def run(self):
        self.initialize_particles()
        progress = []
        
        for _ in range(self.max_iter):
            for particle in self.particles:
                self.update_velocity(particle)
                self.update_position(particle)
            progress.append(self.global_best_distance)
            
        return Route(self.global_best_position), progress
