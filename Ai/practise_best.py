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


heurestic={
    'A':40,
    'B':32,
    'C':25,
    'D':35,
    'E':19,
    'F':17,
    'G':0,
    'H':10,
}

visited=[]

def best(node):
    visited.append(node)
    if node==find:
        print("Node found")
        print(visited)
        exit(0)
    min=1000
    for neighbour in graph[node]:
        if min>heurestic[neighbour]:
            nextnode=neighbour
            min=heurestic[neighbour]
    best(neighbour)


find=input("Enter Goal Node")
node=input("Enter Start node")
best(node)
