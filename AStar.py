
def CostPath(path):
    Gn=0
    for (i , cost) in path:
        Gn+=cost
    #ABCD   -> get last node D and get H(n) Cost
    return Gn + heuristic[path[-1][0]]
def AStarSearch(graph,start,goal):
    if start not in list(graph.keys()):
        return False
    queue=[[(start,0)]]
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
        queue.sort(key=CostPath)
graph = {
         'A': {'C':5,'B':1,'K':2},
         'B':{'C':1},
         'C': {'L':4},
         'K': {'L':3}
         }
heuristic={
    'A':6,
    'K':4,
    'C':7,
    'B':12,
    'L':0
}
path = AStarSearch(graph,'A','L')
if path:
    print("found Solution :",path)
    print("and the cost is :",CostPath(path))
else:
    print("error message")
