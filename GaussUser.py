import numpy as np

def gauss_elimination(A, B):
    n = len(B)
    Aug = np.hstack((A, B.reshape(-1,1))).astype(float)
    for i in range(n):
        if Aug[i][i] == 0:
            for j in range(i+1, n):
                if Aug[j][i] != 0:
                    Aug[[i, j]] = Aug[[j, i]]
                    break
        for j in range(i+1, n):
            factor = Aug[j][i] / Aug[i][i]
            Aug[j, i:] = Aug[j, i:] - factor * Aug[i, i:]
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (Aug[i][-1] - np.dot(Aug[i][i+1:n], X[i+1:n])) / Aug[i][i]
    return X

n = int(input("Enter number of variables: "))

A = []
print("Enter coefficients row by row:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

B = list(map(float, input("Enter constant values: ").split()))

A = np.array(A)
B = np.array(B)

solution = gauss_elimination(A, B)

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {solution[i]:.4f}")
