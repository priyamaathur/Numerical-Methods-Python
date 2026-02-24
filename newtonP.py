import math
def f(x):
    return eval(func,{"x":x,"math":math})
def df(x,h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)
def find_initial_guess(start=-10,end=10,step=0.5):
    x=start
    while x<end:
        try:
            if f(x)*f(x+step)<0:
                return (x+x+step)/2
        except:
            pass
        x+=step
    return None
def newton_raphson(x0,tol,max_iter=50):
    print("Iter\t x_n\t\t f(x_n)\t\t Error")
    print("-"*70)
    for i in range(1,max_iter+1):
        fx=f(x0)
        dfx=df(x0)
        if abs(dfx)<1e-8:
            print("Derivative too close to zero. Method fails.")
            return None
        x1=x0-fx/dfx
        error=abs(x1-x0)
        print(f"{i}\t {x0:.6f}\t {fx:.6f}\t {error:.6f}")
        if error<tol:
            return x1
        x0=x1
    print("Did not converge within maximum iterations.")
    return None
func=input("Enter function f(x): ")
tol=float(input("Enter tolerance: "))
x0=find_initial_guess()
if x0 is None:
    print("Failed to find a suitable initial guess.")
else:
    print(f"\nInitial guess automatically selected: x0 = {x0:.6f}\n")
    root=newton_raphson(x0,tol)
    print("\nApproximate Root:",root)
