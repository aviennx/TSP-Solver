import pandas as pd
from .utils import City

def load_cities_from_csv(file_path):
    df = pd.read_csv(file_path)
    cities = []
    for _, row in df.iterrows():
        cities.append(City(row['x'], row['y']))
    return cities

def generate_random_cities(num_cities, x_range=(0, 100), y_range=(0, 100)):
    import random
    cities = []
    for _ in range(num_cities):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        cities.append(City(x, y))
    return cities
