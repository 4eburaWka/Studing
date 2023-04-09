from math import sqrt

n = int(input("Введите частоту : "))

a, b = 0, 3
d = (b - a) / n

y = 0
x = a

for i in range(n - 1):
    y += (x + i * d) / sqrt(1 + x + i * d)

t =(y * d)



