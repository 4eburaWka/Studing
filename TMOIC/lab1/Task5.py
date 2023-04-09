def Grey(n):
    if n == 0:
        return ['']
    A = []
    for x in range(len(Grey( n- 1))):
        A.append('0' + Grey(n - 1)[x])
    for x in range(len(Grey(n - 1)) - 1, -1, -1):
        A.append('1' + Grey(n - 1)[x])
    return A
    
n = 5
for i in range(2 ** n):
    print(Grey(n)[i])