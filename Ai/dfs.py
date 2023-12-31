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
def dfs(graph, start, goal, visited=None, path=None):
    # initialize visited and path if not provided
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # mark the current node as visited and add it to the path
    visited.add(start)
    path.append(start)

    # base case: goal node found, return the path
    if start == goal:
        return path

    # recursive case: visit unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            # recurse on the neighbor
            new_path = dfs(graph, neighbor, goal, visited, path)
            if new_path is not None:
                # goal node found, return the path
                return new_path

    # goal node not found from this node, backtrack and remove from path
    path.pop()
    return None

node =input("start node: ")
goal =input("goal node: ")
path = dfs(graph, node, goal)
if path:
    print(f"Shortest path from {node} to {goal}: {' -> '.join(path)}")
else:
    print(f"No path found from {node} to {goal}")
