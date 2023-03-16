
def uniform_cost_search(goal, graph):
    visited=[]
    queue=[[list(graph.keys())[0]]] # find root for tree here -->its dict the root ->first key
    while queue:
        node = queue.pop()
        v=node[-1]
        if v in visited:
            continue
        visited.append(v)
        if v == goal:
            return (node,visited)
        for i in graph.get(v,[]):
            temp=list(node)
            temp.append(i)
            queue.append(temp)
    return (False,False)

print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
graph = {'A': ['Y','B','C'],
         'Y':['C'],
         'B': ['C','D'],
         'C': ['D','G'],
         'D': ['C','E'],
         'E': ['F'],
         'F':['K','L']
        }
path,visited=uniform_cost_search('F',graph)

if path:
    print(("find goal the path is :", path, "and the visited node is :", visited))
else:
    print("cannt find this goal")

