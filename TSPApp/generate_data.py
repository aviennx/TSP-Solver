import numpy as np
import pandas as pd

# Generate sample cities
def generate_sample_cities(num_cities=20):
    np.random.seed(42)
    x = np.random.uniform(0, 100, num_cities)
    y = np.random.uniform(0, 100, num_cities)
    
    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv('sample_cities.csv', index=False)
    print(f'Generated {num_cities} cities and saved to sample_cities.csv')

if __name__ == '__main__':
    generate_sample_cities()
