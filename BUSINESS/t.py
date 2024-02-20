def NPV(n, CFn, i, I0):
    res = 0
    for j in range(n):
            res += CFn/((1+i)**(j+1))
    return res - I0


def PI(n, CFn, i, I0):
    res = 0
    for j in range(n):
            res += CFn/((1+i)**(j+1))
    return res / I0


n = 15
CFn=160000
i=0.15
I0=160000
CFn=30000

print(NPV(n, CFn, i, I0))
print(PI(n, CFn, i, I0))