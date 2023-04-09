import collections

def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 
    return list(visited)

def find_num(graph):
    num = 1
    vertexes = list(graph.keys()) # Все вершины
    while True:
        bfs_list = bfs(graph, vertexes[0]) # Все посещенные вершины, стартуя с vertexes[0]
        for x in bfs_list:
            vertexes.remove(x)
        if len(vertexes) == 0: 
            return num
        num += 1
            


graph = {1: [2,3], 2: [1,3], 3: [1,2,4,5], 4: [3,5], 5:[3,4,6], 6:[5],7:[8],8:[7]} 
print(bfs(graph,1))#find_num(graph))

