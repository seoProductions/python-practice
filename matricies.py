
import numpy as np


#input as comma seperated values (CSV)
given = [ float(x) for x in input("Vector to project: ").split(",") ]
vector_y = np.array(given)

given = [ float(x) for x in input("1st basis for W: ").split(",") ]
vector_u1 = np.array(given)

given =  [ float(x) for x in input("2nd basis for W: ").split(",") ]
vector_u2 = np.array(given)

print("Given:")
print(f"y = {vector_y}, β1 = {vector_u1}, β2 = {vector_u2}")


## find constants α
alpha1 = (np.dot(vector_y, vector_u1) / np.dot(vector_u1, vector_u1))
alpha2 = (np.dot(vector_y, vector_u2) / np.dot(vector_u2, vector_u2))

print()
print(f"Projected vector y onto β1 is: {alpha1*vector_u1}")
print(f"Projected vector y onto β2 is: {alpha2*vector_u2}")

# ŷ = α1u1 + α2u2
vector_y_hat = alpha1*vector_u1 + alpha2*vector_u2

print(f"y = {vector_y}")
print(f"ŷ = {vector_y_hat}")
print(f"z = { vector_y - vector_y_hat }, orthogonal to vector space W")

print(f"Vector Y is { np.linalg.norm(vector_y - vector_y_hat) } units from vector space W")