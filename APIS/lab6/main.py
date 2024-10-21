class Node:
    def __init__(self, vertex):
        self.vertex = vertex 
        self.next = None  
        
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [None] * num_vertices
    
    def add_edge(self, src, dest):
        node = Node(dest)
        node.next = self.adj_list[src]
        self.adj_list[src] = node

        node = Node(src)
        node.next = self.adj_list[dest]
        self.adj_list[dest] = node

    def print_graph(self):
        for i in range(self.num_vertices):
            print(f"Вершина {i}:", end="")
            temp = self.adj_list[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print("")
    
    def show(self):
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

        for i in range(self.num_vertices):
            temp = self.adj_list[i]
            while temp:
                matrix[i][temp.vertex] = 1
                temp = temp.next

        for row in matrix:
            print(', '.join(map(str, row)))

def dfs(graph, v, w, visited, path):
    path.append(v)
    visited[v] = True
    
    if v == w:
        return True

    temp = graph.adj_list[v]
    while temp:
        if not visited[temp.vertex]:
            if dfs(graph, temp.vertex, w, visited, path):
                return True
        temp = temp.next

    path.pop()
    return False

def find_path(graph, v, w):
    visited = [False] * graph.num_vertices 
    path = []  
    
    if dfs(graph, v, w, visited, path):
        print("Простой путь из вершины", v, "в вершину", w, ":", path)
    else:
        print("Путь из вершины", v, "в вершину", w, "не существует")

g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)

g.print_graph()
g.show()

v = 0  # Начальная вершина
w = 3  # Целевая вершина
find_path(g, v, w)
