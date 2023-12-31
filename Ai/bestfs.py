graph={
    'A':['B','C','D'],
    'B':['A','E'],
    'C':['A','E','F'],
    'D':['A','F'],
    'E':['B','C','H'],
    'F':['D','C','G'],
    'G':['F','H'],
    'H':['E','G'],
}

heuristics = {
    'A':40,
    'B':32,
    'C':25,
    'D':35,
    'E':19,
    'F':17,
    'G':0,
    'H':10,
}

visited = []

def bfs(node):
    visited.append(node) #addinging node in visited array

    if node == find:
        print("node found")
        print(visited)
        exit(0)

    min = 1000
    for neighbour in graph[node]:
        if min > heuristics[neighbour]:
            nextNode = neighbour
            min = heuristics[neighbour]

    bfs(nextNode)
node=input("enter the starting node: ")
find = input("enter the node to find: ")
bfs(node)
print("not found")

