def gen(pos, p, used):
    if pos == len(A):
        for i in range(len(A)):
            print(A[p[i]], end=' ')
            if (i + 1) % len(A) == 0:
                print()

    for i in range(len(A)):
        if not used[i]:
            used[i] = True
            p[pos] = i
            gen(pos+1, p, used)
            p[pos] = 0
            used[i] = False


A = [1,2,3]
used = [False for x in range(len(A))]
p = [0 for x in range(len(A))]

gen(0, p, used)

# def generate(A, n):
#     if n == 1:
#         print(A)
#         return
#     for x in range(n):
#         generate(A, n-1)
#         if n%2 == 0:
#             A[x], A[n-1] = A[n-1], A[x]
#         else:
#             A[0], A[n-1] = A[n-1], A[0]
    

# A = [x+1 for x in range(3)]
# generate(A, len(A))