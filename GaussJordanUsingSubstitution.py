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

Aug = np.hstack((A, B.reshape(-1, 1)))


for i in range(n):

    if Aug[i][i] == 0:
        for j in range(i+1, n):
            if Aug[j][i] != 0:
                Aug[[i, j]] = Aug[[j, i]]
                break


    Aug[i] = Aug[i] / Aug[i][i]


    for j in range(n):
        if i != j:
            factor = Aug[j][i]
            Aug[j] = Aug[j] - factor * Aug[i]


solution = Aug[:, -1]

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {solution[i]:.4f}")