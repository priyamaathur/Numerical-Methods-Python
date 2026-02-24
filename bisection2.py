import math
def f(x):
    return eval(func, {"x": x, "math": math})
def find_interval(start=-10, end=10, step=0.5):
    x = start
    while x < end:
        try:
            if f(x) * f(x + step) < 0:
                return x, x + step
        except:
            pass
        x += step
    return None, None
def bisection(a, b, tol, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Invalid interval: No sign change.")
        return None
    print("Iter\t a\t\t b\t\t c\t\t f(c)\t\t Error")
    print("-" * 80)
    prev_c = None
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        if prev_c is None:
            error = "-"
        else:
            error = abs(c - prev_c)
        print(i, "\t", f"{a:.6f}", "\t", f"{b:.6f}", "\t",
              f"{c:.6f}", "\t", f"{fc:.6f}", "\t",
              error if error == "-" else f"{error:.6f}")
        if prev_c is not None and error < tol:
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        prev_c = c
    print("Did not converge within maximum iterations.")
    return c
func = input("Enter function f(x): ")
tol = float(input("Enter tolerance: "))
a, b = find_interval()
if a is None:
    print("Failed to find a suitable interval.")
else:
    print(f"\nInterval automatically selected: a = {a:.6f}, b = {b:.6f}\n")
    root = bisection(a, b, tol)
    print("\nApproximate Root:", root)
