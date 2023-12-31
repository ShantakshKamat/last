GRAPH = {
    'panjim':(15,[('ribandar',6),('santa-cruz',9)]),
    'santa-cruz':(12,[('bambolim',7)]),
    'ribandar':(9,[('old-goa',8)]),
    'old-goa':(7,[('corlim',5)]),
    'bambolim':(11,[('old-goa',12),('goa-velha',8)]),
    'corlim':(5,[('kundaim',9)]),
    'kundaim':(2,[('farmagudi',10)]),
    'goa-velha':(10,[('cortalim',10)]),
    'cortalim':(7,[('margao',25),('rachoi',10)]),
    'rachoi':(2,[('farmagudi',12)]),
    'margao':(3,[('farmagudi',20)]),
    'farmagudi':(0,[])
}
start_node = 'panjim'
stop_node = 'farmagudi'
open_list = set([start_node])
close_list = set()
dist = {}
parents = {}
dist[start_node] = 0
parents[start_node] = start_node
while len(open_list) > 0:
    temp = None
    for v in open_list:
        if temp == None or dist[v] + GRAPH[v][0] < dist[temp] + GRAPH[temp][0]:
            temp = v
        if temp == stop_node or len(GRAPH[temp][1]) == 0:
            pass
    else:
        for (m,wt) in GRAPH[temp][1]:
            if m not in open_list and m not in close_list:
                open_list.add(m)
                parents[m] = temp
                dist[m] = dist[temp] + wt
            else:
                if dist[m] > dist[temp] + wt:
                    dist[m] = dist[temp] + wt
                    parents[m] = temp
                    if m in close_list:
                        close_list.remove(m)
                        open_list.add(m)
    if temp == None:
        print("Path does not exist")
        break
    if temp == stop_node:
        path = []
        while parents[temp] != temp:
            path.append(temp)
            temp = parents[temp]
        path.append(start_node)
        path.reverse()
        print(f"\n\nPath : {path}")
        break
    print(f"Open list : {open_list}")
    print(f"Close list : {close_list}")
    open_list.remove(temp)
    close_list.add(temp)
else:
    print("Path does not exist")
