def gen(n, k):
    a = [x for x in range(n+1)]
    b = [x for x in range(k+1)]
    
    q = k
    while q >= 1:
        for j in range(1, k+1, 1):
            print(a[b[j]], end='')
        print(end='\t')
        if b[k] == n:
            q -= 1
        else:
            q = k
        
        if q >= 1:
            b[q] += 1
            for i in range(q+1, k+1,1):
                b[i] = b[i-1] + 1


gen(6,4)