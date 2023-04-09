def f(x):
    return x ** 3 + 8 * x ** 2 - 3 * x - 9
def df(x):
    return 3 * x ** 2 + 16 * x - 3

# метод половинного деления с выводом каждого шага a, b, x
def half_division(a, b, eps):
    print("a\tb\tx\tf(a)*f(x)")
    while abs(b - a) > eps:
        x = (a + b) / 2
        print(f"{a:.4f}\t{b:.4f}\t{x:.4f}\t{f(a)*f(x)}")
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return x
half_division(1, 2, 0.01)

# метод хорд с выводом каждого шага 
def chords(x0, C, eps):
    x1 = x0 - (C-x0) * f(x0)/(f(C)-f(x0))
    print(x0)
    print(x1)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - (C-x0) * f(x0)/(f(C)-f(x0))
        print(x1)
    return x1
chords(1, 2, 0.01)

# метод Ньютона с выводом каждого шага
def newton(x0, eps):
    x1 = x0 - f(x0)/df(x0)
    print(x0)
    print(x1)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - f(x0)/df(x0)
        print(x1)
    return x1
newton(1, 0.01)

