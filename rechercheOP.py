# Import PuLP module
import pulp

# Create a problem instance
prob = pulp.LpProblem("LinearProgrammingProblem", pulp.LpMaximize)

# Define decision variables
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

# Define objective function
obj = 100*x1 + 200*x2
prob += obj

# Define constraints
prob += 4*x1 + 3*x2 <= 240  # Constraint 1
prob += 2*x1 + x2 <= 100   # Constraint 2
prob += x2 <= 60           # Constraint 3

# Solve the problem using CBC solver
prob.solve()

# Print the optimal solution
print("Status:", pulp.LpStatus[prob.status])
print("Objective:", pulp.value(obj))
print("x1:", pulp.value(x1))
print("x2:", pulp.value(x2))
