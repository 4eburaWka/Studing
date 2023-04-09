import time
start = time.time()
def dijkstra(graph, src):
    src -= 1
    visited = []
    distance = {src+1: 0}
    node = list(range(len(graph[0])))
    if src in node:
        node.remove(src)
        visited.append(src)
    else:
        return None
    for i in node:
        distance[i+1] = graph[src][i]
    prefer = src
    while node:
        _distance = float('inf')
        for i in visited:
            for j in node:
                if graph[i][j] > 0:
                    if _distance > distance[i+1] + graph[i][j]:
                        _distance = distance[j+1] = distance[i+1] + graph[i][j]
                        prefer = j
        visited.append(prefer)
        node.remove(prefer)
    return distance

graph = [
    [0, 5, 0, 6, 8, 0, 0],
    [5, 0, 6, 3, 0, 0, 0],
    [0, 6, 0, 6, 0, 0, 0],
    [6, 3, 6, 0, 4, 2, 0],
    [8, 0, 0, 4, 0, 0, 5],
    [0, 0, 0, 2, 0, 0, 3],
    [0, 0, 0, 0, 5, 3, 0]
]
print(dijkstra(graph, 1))
# print(f"Алгоритм Дейкстра выполняется за {0.0000970664978027344} секунд")