
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
        print(path)
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
         'A': {'B':21,'C':22,'D':19},
         'B':{'C':4,'E':11},
         'C': {'E':4,'B':4,'F':12,'D':6},
         'E': {'G':7,'C':4,'F':2},
    'F':{'D':7,'C':12,'E':2,'G':9}
         }
heuristic={
    'A':34,
    'B':19,
    'C':14,
    'D':18,
    'E':7,
    'F':9,
    'G':0
}
print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
path = AStarSearch(graph,'A','G')
if path:
    print("found Solution :",path)
    print("and the cost is :",CostPath(path))
else:
    print("error message")
