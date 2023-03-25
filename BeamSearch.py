

def BeamSearch(graph,start,goal,heuristic,n):
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
            PQ=[]
            for i in Child:
                pathnode=path + [(i,heuristic[i])]
                PQ.append(pathnode)
            PQ.sort(key=lambda x:heuristic[x[-1][0]])
            for i in range(n):
                if PQ:
                   queue.append(PQ.pop(0))
                else:
                    break
        queue.sort(key=lambda x:heuristic[x[-1][0]])
graph = {
         'A': {'C','B','S'},
         'B':{'D','F','J'},
         'F': {'W','Y','Z'},
         'W': {'L','Q'}
         }
heuristic={
    'A':6,
    'C':9,
    'B':8,
    'S':10,
    'D':7,
    'F':6,
    'J':11,
    'W':10,
    'Y':6,
    'Z':7,
    'L':3,
    'Q':0
}
path = BeamSearch(graph,'A','L',heuristic,3)
if path:
    print("found Solution :",path)
else:
    print("error message")
