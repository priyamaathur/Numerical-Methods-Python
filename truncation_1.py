import math

print("Truncation Error Demonstration (Easy Level)")

x = math.pi / 6

true_value = math.sin(x)

approx_value = x - (x**3) / math.factorial(3)

print("Actual sin(", x, ") =", true_value)
print("Approximation =", approx_value)
print("Truncation error =", abs(true_value - approx_value))