#DFS

#Implement depth first search algorithm and Breadth First Search
#algorithm, use an undirected graph and develop a recursive algorithm for searching all the
#vertices of a graph or tree data structure.

graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("DFS is: ")
dfs(visited, graph, '5')


#BFS

graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS is: ")
bfs(visited, graph, '5')
