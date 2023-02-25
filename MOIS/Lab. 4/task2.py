A = range(1,11,1)

for x in range(10):
    for y in range(10):
        print((A[x]*A[y]) % 11, end=' ')
    print()
