import heapq
def uniform_cost_search(start, goal, graph):
    visited =[]
    priorityQueue = [(0, start, [])]
    while priorityQueue:

        (cost, node, x) = heapq.heappop(priorityQueue)#return path has smallest cost
        path=list(x)
        if node not in visited:
            visited.append(node)
           # path= path +[node]    #path.append(node) what is deferent  about path=path + [node]?????
            path.append(node)# this is error while i use path=path+[node] become right ? why
            #I found it when the addition is used. This works on adding to the original list, and this is wrong. In every case, the list must be updated.
            #now U can use two approach  and two is right
            if node == goal:
                return (cost, path,visited)
            for i in graph.get(node,[]):
                if i not in visited:
                    total_cost = cost + graph[node][i]
                    heapq.heappush(priorityQueue,(total_cost, i, path))

    return (False,False,False)

print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
graph = {'A': {'B':2, 'C':5},
     'B': {'C':2, 'D':5},
     'C': {'D':4, 'G':2},
     'D': {'C':6, 'E':4},
     'E': {'F':1},
     'F':{'K':3,'L':4}

  }
cost,path,visited = uniform_cost_search('A','E', graph)
if cost:
    print(("the cost is :",cost," and the path is :",path,"and the visited node is :",visited))
else:
    print('goal is not found')









