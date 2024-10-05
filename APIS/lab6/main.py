class Node:
    def __init__(self, vertex):
        self.vertex = vertex  # Вершина
        self.next = None  # Указатель на следующий узел

# Класс графа с использованием списка смежности
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # Массив указателей на список соседей (изначально None)
        self.adj_list = [None] * num_vertices
    
    # Функция добавления ребра
    def add_edge(self, src, dest):
        # Добавляем вершину dest к списку смежности вершины src
        node = Node(dest)
        node.next = self.adj_list[src]
        self.adj_list[src] = node

        # Поскольку граф неориентированный, добавляем ребро в обратном направлении
        node = Node(src)
        node.next = self.adj_list[dest]
        self.adj_list[dest] = node

    # Функция для отображения списка смежности графа
    def print_graph(self):
        for i in range(self.num_vertices):
            print(f"Вершина {i}:", end="")
            temp = self.adj_list[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print("")
    
    def show(self):
        # Инициализируем пустую матрицу смежности размером num_vertices x num_vertices
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

        # Заполняем матрицу на основе списка смежности
        for i in range(self.num_vertices):
            temp = self.adj_list[i]
            while temp:
                matrix[i][temp.vertex] = 1
                temp = temp.next

        # Выводим матрицу
        for row in matrix:
            print(', '.join(map(str, row)))

# Функция для выполнения поиска в глубину (DFS)
def dfs(graph, v, w, visited, path):
    # Добавляем текущую вершину в путь
    path.append(v)
    visited[v] = True
    
    # Если достигли целевой вершины, возвращаем путь
    if v == w:
        return True

    # Проходим по всем соседям текущей вершины
    temp = graph.adj_list[v]
    while temp:
        if not visited[temp.vertex]:
            if dfs(graph, temp.vertex, w, visited, path):
                return True
        temp = temp.next

    # Если не нашли путь, удаляем вершину из пути и возвращаем False
    path.pop()
    return False

# Основная функция для поиска простого пути
def find_path(graph, v, w):
    visited = [False] * graph.num_vertices  # Массив для отслеживания посещенных вершин
    path = []  # Путь, который мы строим
    
    if dfs(graph, v, w, visited, path):
        print("Простой путь из вершины", v, "в вершину", w, ":", path)
    else:
        print("Путь из вершины", v, "в вершину", w, "не существует")

# Пример использования
g = Graph(5)

# Добавляем рёбра
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)

# Выводим граф
# g.print_graph()
g.show()

# Вызов функции для поиска пути
v = 0  # Начальная вершина
w = 3  # Целевая вершина
find_path(g, v, w)
