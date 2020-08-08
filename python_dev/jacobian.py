import symengine
vars = symengine.symbols('a b') # Define x and y variables
f = symengine.sympify(['A * cos(a) + B * cos(a+b)', 'A * sin(a) + B * sin(a + b)']) # Define function
J = symengine.zeros(len(f),len(vars)) # Initialise Jacobian matrix

# Fill Jacobian matrix with entries
for i, fi in enumerate(f):
    for j, s in enumerate(vars):
        J[i,j] = symengine.diff(fi, s)
print J
