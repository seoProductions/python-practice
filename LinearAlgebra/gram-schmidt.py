# Calculate Gram-Schmidt orthogonal vector basis from any given
# vector.
# This is done via Gram's Algorithm in Linear Algebra
#

import numpy as np


#input as comma seperated values (CSV)
given = [ float(x) for x in input("1st basis vector: ").split(",") ]
vector_x1 = np.array(given)

given = [ float(x) for x in input("2nd basis vector: ").split(",") ]
vector_x2 = np.array(given)

given = [ float(x) for x in input("3nd basis vector: ").split(",") ]
vector_x3 = np.array(given)

print("Given:")
print(f"β1 = {vector_x1}, β2 = {vector_x2}, β3 = {vector_x3}")

# find orthogonal basis of vectors
v1 = vector_x1
v2 = vector_x2 - ((np.dot(vector_x2, v1) / np.dot(v1, v1))*v1)
v3 = vector_x3 - ((np.dot(vector_x3, v1) / np.dot(v1, v1))*v1) - ((np.dot(vector_x3, v2) / np.dot(v2, v2))*v2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")

print(f"normalized v1 = {v1 / np.linalg.norm(v1)}")
print(f"normalized v2 = {v2 / np.linalg.norm(v2)}")
print(f"normalized v3 = {v3 / np.linalg.norm(v3)}")

