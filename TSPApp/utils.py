import numpy as np

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        return np.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)

class Route:
    def __init__(self, cities):
        self.cities = cities
        self.distance = self.calculate_distance()
    
    def calculate_distance(self):
        total_distance = 0
        for i in range(len(self.cities)):
            total_distance += self.cities[i].distance(self.cities[(i+1) % len(self.cities)])
        return total_distance
