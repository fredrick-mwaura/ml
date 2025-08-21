import math
import random

def simulated_annealing(initial_solution, cost_function, neighbor_function, schedule, max_iter=1000):
    current = initial_solution
    current_cost = cost_function(current)

    for t in range(1, max_iter + 1):
        T = schedule(t)
        
        """check for unprocessable value Of T"""
        if T <= 0:
            break

        neighbor = neighbor_function(current)
        neighbor_cost = cost_function(neighbor)
        delta_e = neighbor_cost - current_cost
        
        """ better solution"""
        if delta_e < 0:
            current, current_cost = neighbor, neighbor_cost
        else:
            # accept worse solution with some probability
            if random.random() < math.exp(-delta_e / T):
                current, current_cost = neighbor, neighbor_cost

    return current, current_cost
"""
use cases:
- salesmen routes - 
"""