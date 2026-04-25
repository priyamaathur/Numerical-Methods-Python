import numpy as np

def divided_difference(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x[j:n] - x[0:n-j])
    return coef

def newton_polynomial(coef, x_data, x):
    n = len(coef)
    result = coef[0]
    product = 1.0
    for i in range(1, n):
        product *= (x - x_data[i-1])
        result += coef[i] * product
    return result

x_data = np.array([1, 2, 4, 5])
y_data = np.array([1, 4, 16, 25])
x_value = 3

coefficients = divided_difference(x_data, y_data)
y_value = newton_polynomial(coefficients, x_data, x_value)

print(coefficients)
print(round(y_value, 4))