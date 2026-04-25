def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0
    print("x\t\ty")
    print(f"{x:.4f}\t{y:.6f}")
    
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        
        print(f"{x:.4f}\t{y:.6f}")


f = lambda x, y: x * y + x**3

x0 = 0
y0 = 1   
h = 0.1
n = 10

runge_kutta(f, x0, y0, h, n)