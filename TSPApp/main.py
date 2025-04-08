import argparse
from .data_loader import load_cities_from_csv, generate_random_cities
from .genetic import GeneticAlgorithm
from .pso import PSO
from .antcolony import ACO
from .visualization import plot_route

"""
TSP Solver - A Python implementation of the Traveling Salesman Problem
using various optimization algorithms.

This module provides a command-line interface to solve TSP using:
- Genetic Algorithm
- Particle Swarm Optimization (PSO)
- Ant Colony Optimization (ACO)

Example usage:
    python -m TSPApp.main --algorithm genetic --cities 20
    python -m TSPApp.main --algorithm pso --cities 30
    python -m TSPApp.main --algorithm aco --csv cities.csv
"""

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='TSP Solver using various algorithms')
    parser.add_argument('--algorithm', choices=['genetic', 'pso', 'aco'], required=True,
                      help='Algorithm to use for solving TSP')
    parser.add_argument('--cities', type=int, default=20,
                      help='Number of cities to generate (if not using CSV)')
    parser.add_argument('--csv', type=str, help='CSV file containing city coordinates')
    parser.add_argument('--iterations', type=int, default=500,
                      help='Number of iterations to run')
    parser.add_argument('--show-progress', action='store_true',
                      help='Show optimization progress plot')
    return parser.parse_args()

def main():
    """Main function to run the TSP solver."""
    args = parse_arguments()
    
    # Load or generate cities
    if args.csv:
        cities = load_cities_from_csv(args.csv)
    else:
        cities = generate_random_cities(args.cities)
    
    # Run selected algorithm
    if args.algorithm == 'genetic':
        solver = GeneticAlgorithm(cities)
        best_route, progress = solver.run(generations=args.iterations)
    elif args.algorithm == 'pso':
        solver = PSO(cities)
        best_route, progress = solver.run()
    else:  # aco
        solver = ACO(cities)
        best_route, progress = solver.run()
    
    # Visualize results
    plot = plot_route(best_route, 
                     title=f'TSP Solution using {args.algorithm.upper()}',
                     show_progress=args.show_progress,
                     progress=progress)
    plot.show()

if __name__ == '__main__':
    main()
