import random as rd
a = 3
p = 12

def f(a, x):
    return a ** x % p

# пользователь i
Xi = rd.randint(1, p-1)
Yi = f(a, Xi)
Zij = f(Yi, Xi)

# пользователь j
Xj = rd.randint(1, p-1)
Yj = f(a, Xj)
Zji = f(Yi, Xj)

if Zij == Zji:
    print("Пользователи найдены")
else:
    print("Пользователи не найдены")

    