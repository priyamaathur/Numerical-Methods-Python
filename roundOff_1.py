import math

print("Round-off Error Demonstration (Easy Level)")

a = 1.0
b = 1e-10

sum_true = 1.0000000001
sum_float = a + b

print("1 + 1e-10 =", sum_float)
print("Expected sum:", sum_true)
print("Round-off error:", abs(sum_true - sum_float))