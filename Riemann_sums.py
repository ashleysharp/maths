def f(x):
    result = x
    return result

def dx(a, b, n):
    result = (b-a)/n
    return result

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

