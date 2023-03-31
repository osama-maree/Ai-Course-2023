
#here write my code

def HandG(p):
    Gn=0
    for i,c in p:
        Gn=Gn+c
    return Gn+heuristic[p[-1][0]]

def Astar(graph,start,goal,heuristic):

    Q=[[(start,0)]]
    visited=[]
    while Q:
        path=Q.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            child=graph.get(node,[])
            for i in child:
                p=path+[(i,child[i])]#grapg[node][i]
                Q.append(p)
        Q.sort(key=HandG)

graph = {
         'A': {'C':5,'B':1,'K':2},
         'B':{'C':1},
         'C': {'L':4},
         'K': {'L':3}
         }
heuristic={
    'A':6,
    'K':4,
    'C':3,
    'B':1,
    'L':0
}
path = Astar(graph,'A','L',heuristic)
if path:
    print("found Solution :",path)
    print("Cost is",HandG(path))
else:
    print("error message")