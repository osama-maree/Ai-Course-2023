

def GreedySearch(graph,start,goal,heuristic):
    if start not in list(graph.keys()):
        return False
    queue=[[(start,heuristic[start])]]
    visited=[]
    while queue:
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            Child=graph.get(node,[])
            for i in Child:
                pathnode=path + [(i,Child[i])]
                queue.append(pathnode)
        queue.sort(key=lambda x:heuristic[x[-1][0]])
graph = {
         'A': {'C':5,'B':1,'K':2},
         'B':{'C':1},
         'C': {'L':4},
         'K': {'L':3}
         }
heuristic={
    'A':6,
    'K':4,
    'C':10,
    'B':1,
    'L':0
}
path = GreedySearch(graph,'A','L',heuristic)
if path:
    print("found Solution :",path)
else:
    print("error message")
