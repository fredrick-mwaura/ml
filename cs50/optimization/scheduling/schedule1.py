"""using library"""
# conda install -c conda-forge python-constraint
#pip install python-contraint
from constraint import *

problem = Problem()

# Add variables
problem.addVariables(
    ["A", "B", "C", "D", "E", "F", "G"],
    ["Monday", "Tuesday", "Wednesday"]
) # (self, variables, domain)

# Add constraints
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]
for x, y in CONSTRAINTS:
    """lambda
    def n(x,y):
        return x != y, (x, y)
    """
    problem.addConstraint(lambda x, y: x != y, (x, y))

# Solve problem
for solution in problem.getSolutions(): # (self)
    print(solution)
