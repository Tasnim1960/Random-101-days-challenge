graph = {
    0: [1, 2, 3],
    1: [0, 1],
    2: [0, 1, 4],
    3: [0],
    4: [2]
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for i in graph[vertex]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


bfs(visited, graph, 0)




