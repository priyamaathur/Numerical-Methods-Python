import math

def f(x):
    return math.sin(x)

def simpson_one_third(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)
    
    result *= h / 3
    return result

# User input
a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))

while True:
    n = int(input("Enter number of intervals (even n): "))
    if n > 0 and n % 2 == 0:
        break
    print("Invalid input! n must be a positive EVEN number.")

integral = simpson_one_third(a, b, n)
print("Simpson’s 1/3rd Method (sin(x)):", integral)