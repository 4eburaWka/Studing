import time
start = time.time()
from math import inf

def get_path(P, u, v):
    path = [u]
    while u != v:
        u = P[u][v]
        path.append(u)
    return path


V = [
    [inf, 5, inf, 6, 8, inf, 0],
    [5, inf, 6, 3, inf, inf, 0],
    [inf, 6, inf, 6, inf, inf, 0],
    [6, 3, 6, inf, 4, 2, 0],
    [8, inf, inf, 4, inf, inf, 5],
    [inf, inf, inf, 2, inf, inf, 3],
    [inf, inf, inf, inf, 5, 3, 0]
]
N = len(V)
P = [[v for v in range(N)] for u in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = k

print(get_path(P, 2, 0))
# print(f"Алгоритм Флойда выполняется за {time.time()-start} секунд")
