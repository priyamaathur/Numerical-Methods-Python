print("----- Regula–Falsi Method for Polynomial Equation -----")
def f(x):
    return x**2 - 4*x - 5
def regula_falsi(a, b, tolerance=0.00001, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Invalid interval: No sign change.")
        return None
    print("Iter\t   a\t\t   b\t\t   c\t\t f(c)\t\t Error")
    prev_c = None
    for i in range(1, max_iter + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
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
root = regula_falsi(4, 6)
print("\nApproximate Root =", root)

