def f(x):
    return x**3 - x - 2
tolerance = 0.0001
start = -10
end = 10
step = 0.5
a = None
b = None
x = start
while x < end:
    if f(x) * f(x + step) < 0:
        a = x
        b = x + step
        break
    x += step
if a is None:
    print("No suitable interval found")
else:
    print("Initial interval found:")
    print("a =", a, "b =", b)
    prev_c = None
    iteration = 1
    print("\nIter\t a\t\t b\t\t c\t\t Error")
    while True:
        c = (a + b) / 2
        if prev_c is None:
            error = "-"
        else:
            error = abs(c - prev_c)
        print(iteration, "\t", f"{a:.6f}", "\t", f"{b:.6f}", "\t",
              f"{c:.6f}", "\t", error if error == "-" else f"{error:.6f}")
        if prev_c is not None and error < tolerance:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        prev_c = c
        iteration += 1
    print("\nApproximate Root =", f"{c:.6f}")
    print("Tolerance =", tolerance)

