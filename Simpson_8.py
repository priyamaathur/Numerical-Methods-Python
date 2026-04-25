import math

def f(x, choice):
    if choice == 1:
        return x**3 + 2*x + 1
    elif choice == 2:
        return math.cos(x)
    elif choice == 3:
        return math.exp(x)

def simpson_one_third(a, b, n, choice):
    h = (b - a) / n
    result = f(a, choice) + f(b, choice)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x, choice)
        else:
            result += 4 * f(x, choice)
    
    result *= h / 3
    return result

# Menu
print("Choose function:")
print("1. f(x) = x^3 + 2x + 1")
print("2. f(x) = cos(x)")
print("3. f(x) = exp(x)")

choice = int(input("Enter your choice (1/2/3): "))

a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))

while True:
    n = int(input("Enter number of intervals (even n): "))
    if n > 0 and n % 2 == 0:
        break
    print("Invalid input! n must be even.")

result = simpson_one_third(a, b, n, choice)

print("\nOutput:")
if choice == 1:
    print("Simpson’s 1/3rd Method (x^3 + 2x + 1) =", result)
elif choice == 2:
    print("Simpson’s 1/3rd Method (cos(x)) =", result)
elif choice == 3:
    print("Simpson’s 1/3rd Method (exp(x)) =", result)