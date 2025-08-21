from scipy.optimize import linprog
""" core modules
scipy.optimize -> optimization(curve fitting)
scipy.intergrate -> num intergration
scipy.stats -> probabilities distribution
scipy.spatial -> geometry / distances / KD-trees
scipy.signal -> signal processing
scipy.linalg -> linear algebr


Objective Function: 50x_1 + 80x_2
Constraint 1: 5x_1 + 2x_2 <= 20
Constraint 2: -10x_1 + -12x_2 <= -90
linear programing
res = linprog(
    c,             # coefficients of the objective function
    A_ub=None,     # inequality constraint matrix
    b_ub=None,     # inequality constraint vector
    A_eq=None,     # equality constraint matrix
    b_eq=None,     # equality constraint vector
    bounds=None,   # variable bounds (default: x >= 0)
    method='highs' # solver (default = 'highs')
)
"""

result = linprog( #linprog => linear programing
    [50, 80],  # Cost function: 50x_1 + 80x_2
    A_ub=[[5, 2], [-10, -12]],  # Coefficients for inequalities
    b_ub=[20, -90],  # Constraints for inequalities: 20 and -90
)

if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"X2: {round(result.x[1], 2)} hours")
else:
    print("No solution")
