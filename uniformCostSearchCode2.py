
def uniform_cost_search(start,goal, graph, cost ):
    visited=[]
   # priorityQueue=[(0,[list(graph.keys())[0]])] # find root for tree here -->its dict the root ->first key
    priorityQueue=[(0,[start])] # or U can use a bove line and always starts from root
    while priorityQueue:
        cst,node = priorityQueue.pop(0)
        v=node[-1]
        if v in visited:
            continue
        visited.append(v)
        if v == goal:
            return (cst,node)
        for i in graph.get(v,[]):
            temp=list(node)
            temp.append(i)
            total_cost=cst + cost[(v,i)]
            priorityQueue.append((total_cost,temp))
        priorityQueue.sort()
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
costs ={('A','Y'):3,('A','B'):2,('A','C'):5,('Y','C'):2,('B','C'):2,('B','D'):5,('C','D'):4,
       ('C','G'):4,('D','C'):4,('D','E'):4,('E','F'):4,('F','K'):6,('F','L'):8}
start,goal='B','E'
(cost,path)=uniform_cost_search(start,goal,graph,costs)

if path:
    print(("the cost is :",cost," and the path is :",path),end=':((')
else:
    print("cannt find this goal")

