import math

print("----- Regula–Falsi Method for Transcendental Equation -----")

def f(x):
    return x - math.cos(x)

def regula_falsi(a, b, tolerance=0.0001, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Invalid interval: No sign change.")
        return None

    print("Iter\t a\t\t b\t\t c\t\t f(c)\t\t Error")

    prev_c = None

    for i in range(1, max_iter + 1):
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        fc = f(c)

        if prev_c is None:
            error = "-"
        else:
            error = abs(c - prev_c)

        print(i, "\t", f"{a:.6f}", "\t", f"{b:.6f}", "\t",
              f"{c:.6f}", "\t", f"{fc:.6f}", "\t",
              error if error == "-" else f"{error:.6f}")

        if prev_c is not None and error < tolerance:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        prev_c = c

    print("\nTolerance =", tolerance)
    return c


root = regula_falsi(0, 1)
print("Approximate Root =", root)

