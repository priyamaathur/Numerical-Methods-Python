import numpy as np

n = int(input("Enter number of variables: "))

A = []
print("Enter coefficients row by row:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

B = list(map(float, input("Enter constant values: ").split()))

A = np.array(A, dtype=float)
B = np.array(B, dtype=float)

# Solve using NumPy Linear Algebra
solution = np.linalg.solve(A, B)

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {solution[i]:.4f}")