import random

MAX = 101

def min_spanning_tree(graph, start):
    dist = [MAX] * len(graph)
    m = 1
    dist[start] = 0

    print(f"D[0] = {' '.join(map(str, dist))}")

    while True:
        d = [0] * len(graph)
        k = 0

        for i in range(len(graph)):
            minimum = MAX
            for j in range(len(graph)):
                minimum = min(minimum, dist[j] + graph[j][i])
            d[i] = minimum

        print(f"D[{m}] = ", end='')
        for i in range(len(graph)):
            if i != start:
                if dist[i] > d[i]:
                    dist[i] = d[i]
                    k += 1
            print(dist[i], end=' ')
        print()

        m += 1

        if k == 0:
            break

# Закомментированная часть для случайной генерации графа
'''
V = 6
graph = [[0] * V for _ in range(V)]

for i in range(V):
    for j in range(V):
        if i == j:
            graph[i][j] = 0
        elif j < i:
            graph[i][j] = graph[j][i]
        else:
            graph[i][j] = random.randint(1, 100)

for row in graph:
    print(' '.join(map(str, row)))
'''

# Пример статически заданного графа
graph = [
    [0, 2, 7, 4, 6, 3],
    [3, 0, 4, 5, 6, 1],
    [2, 4, 0, 8, 7, MAX],
    [4, MAX, 8, 0, 5, 7],
    [MAX, 7, 8, 4, 0, 3],
    [2, 4, MAX, 7, 8, 0]
]

min_spanning_tree(graph, 3)
