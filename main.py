import heapq
def uniform_cost_search(start, goal, graph):
    visited = []
    priorityQueue = [(0, start, [])]
    while priorityQueue:
        (cost, node, path) = heapq.heappop(priorityQueue)#return path has smallest cost
        if node not in visited:
            visited.append(node)
            path.append(node)    #path.append(node) what is deferent about path=path+[node] ?????
            if node == goal:
                return (cost, path)
            for i in graph.get(node,[]):
                if i not in visited:
                    total_cost = cost + graph[node][i]
                    heapq.heappush(priorityQueue,(total_cost, i, path))

    return (False,False)

# print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
graph = {'A': {'B':2, 'C':5},
     'B': {'C':2, 'D':5},
     'C': {'D':4, 'G':2},
     'D': {'C':6, 'E':4},
     'E': {'F':1},
     'F':{'K':3,'L':4}

  }
cost,path = uniform_cost_search('A','G', graph)
if cost:
    print(("the cost is :",cost," and the path is :",path))
else:
    print('goal is not found')









