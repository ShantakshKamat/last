from collections import deque
# define the graph as a dictionary of lists

graph = {
  'GEC' : {'Cuncoleim Circle','Ponda Bus Stand'},
  'Ponda Bus Stand' : {'GEC', 'Borim Bridge', 'Shakari Spice Farm'},
  'Borim Bridge' : {'Shakari Spice Farm', 'Sanvordem'},
  'Verna Junction' : {'Borim Bridge', 'Cortalim', 'KTC'},
  'Don Bosco' : {'KTC', "Sanvordem"},
  'KTC' : {'Verna Junction', 'Sanvordem'},
  'Cortalim': {'GMC', 'Verna Junction'},
  'Airport': {'Verna Junction', 'Cortalim', 'Chicalim Circle', 'Varunapuri'},
  'Varunapuri': {'Airport','Home'},
  'Chicalim Circle': {'Home', 'Airport', 'Cortalim'},
  'Home': {'Chicalim Circle', 'Varunapuri'},
  'GMC': {'Cortalim', 'Goa University', 'Merces Circle'},
  'Goa University' : {'GMC'},
  'Merces Circle' : {'GMC', 'Panjim', 'Corlim'},
  'Panjim' : {'Merces Circle'},
  'Corlim' : {'Merces Circle', 'Banastarim Bridge'},
  'Banastarim Bridge' : {'Corlim', 'Cuncoleim Circle'},
  'Cuncoleim Circle' : {'GEC', 'Banastarim Bridge'},
  'Shakari Spice Farm' : {'Ponda Bus Stand', 'Borim Bridge'},
  'Sanvordem' : {'Borim Bridge', 'KTC'},
}

def bfs(graph, start, goal):
    # create a queue for BFS
    queue = deque([start])
    # keep track of visited nodes
    visited = set([start])
    # keep track of parent nodes to reconstruct path
    parents = {start: None}

    # perform BFS
    while queue:
        node = queue.popleft()
        if node == goal:
            # goal node found, reconstruct path and return it
            path = []
            while node:
                path.append(node)
                node = parents[node]
            path.reverse()
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parents[neighbor] = node

    # goal node not found
    return None

# example usage
start_node =input("start node: ")
goal_node =input("goal node: ")
path = bfs(graph, start_node, goal_node)
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
