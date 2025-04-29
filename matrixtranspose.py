# perform matrix transpositions for linear algebra
# very nice and handy

import numpy as np


#input as comma seperated values (CSV)
given = [ float(x) for x in input("1st basis for W: ").split(",") ]
vector_u1 = np.array(given)

given =  [ float(x) for x in input("2nd basis for W: ").split(",") ]
vector_u2 = np.array(given)

print("Given:")
print(f" β1 = {vector_u1}, β2 = {vector_u2}")


## find constants Transposes
B_matrix = np.column_stack((vector_u1, vector_u2)) # (()) create tuple for args
print(B_matrix)

print()
print(f"U^t @ U = { np.transpose(B_matrix) @ B_matrix }")
print(f"U @ U^t = { B_matrix @ np.transpose(B_matrix) }")
