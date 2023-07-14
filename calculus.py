# Load packages
import numpy as np
import sympy as sp
import math

# Single variable

## Derivative
f = lambda x: x**2

def f(x):
    return x**2

def diff(a, n):
    delta_x = 1/n
    delta_y = f(a + delta_x) - f(a)
    result = delta_y/delta_x
    return result

x = sp.Symbol('x')
f = sp.Function('f')
g = sp.Function('g')(x)

expr = x ** 2
expr.subs(x, 3)

f = sp.Lambda(x, x**2)

expr_derivative = sp.diff(expr, x)
expr_derivative.subs(x, f)

## Riemann integral
def f(x):
    return x**2

def dx(a, b, n):
    return (b-a)/n

def riemann_left(a, b, n):
    delta_x = dx(a, b, n)
    total = 0
    for i in range(n):
        total += f(a + i*delta_x)*delta_x
    return total

def riemann_right(a, b, n):
    delta_x = dx(a, b, n)
    total = 0
    for i in range(1, n+1):
        total += f(a + i*delta_x)*delta_x
    return total

x = sp.Symbol('x')
expr = x ** 2

sp.integrate(expr, x)
sp.integrate(expr, (x, 0, 3))

# Multi-variable

def g(x,y):
    return x**2*y**2

def g(t):
    x = np.cos(t)
    y = np.sin(t)
    z = t**2
    return np.array([x,y,z])

x, y, z, t = sp.symbols('x y z t')


vector_expr = sp.Matrix([sp.cos(t), sp.sin(t), t**2])

sp.diff(vector_expr, t)