def EXtr(results, f):
    from random import uniform
    Nmax = 10 # Максимальное количество итераций
    amin = 0.0001 # Минимальный шаг
    a = 0.1 # Начальный шаг

    x0 = 5
    y0 = f(x0)
    while Nmax:
        x1 = x0 + a * uniform(-1, 1)
        y1 = f(x1)

        if y1 < y0:
            x0, y0 = x1, y1

        a *= uniform(0.75, 0.999)
        if a < amin:
            break

        Nmax -= 1
    results.append(y0)