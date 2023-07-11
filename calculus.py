# Load packages
import numpy as np
import sympy as sp


# Single variable

def f(x):
    return x**2

def dx(a, b, n):
    return (b-a)/n

def riemann_left(a, b, n):
    delta_x = (b-a)/n
    total = 0
    for i in range(n):
        total += f(a + i*delta_x)*delta_x
    return total

def riemann_right(a, b, n):
    delta_x = (b-a)/n
    total = 0
    for i in range(1, n+1):
        total += f(a + i*delta_x)*delta_x
    return total

def diff(a, n):
    delta_x = 1/n
    delta_y = f(a + delta_x) - f(a)
    result = delta_y/delta_x
    return result

x = sp.Symbol('x')
f = x ** 2
sp.diff(f, x)

# Multi-variable

def g(x,y):
    return x**2*y**2


lst = [10,20,30,40,50]
vctr = np.array(lst)