from random import uniform

a =[]
for i in range(5):
    d = uniform(0.28, 0.35)
    a.append(d)
    print(d)

print(sum(a)/len(a))