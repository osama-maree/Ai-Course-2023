import  heapq

#under woork not completed
def Hill_Climbing(start,graph):
    path=[start]
    visited=[]
    priorityQueueForNode=[(0,start,path)]
    while priorityQueueForNode:
        d=graph.get(start,[])
        visited.append(start)
        if not d:
            (cst,node,p)=heapq.heappop(priorityQueueForNode)
            path=list(p)
            if node in visited:
                continue
            visited.append(node)
            d=graph.get(node,[])
            if not d:
                continue
        priorityQueue = []
        for i in d:
            heapq.heappush(priorityQueue,(d[i],i))

            heapq.heappush(priorityQueueForNode,(d[i],i,path))
        (cost, i) = heapq.heappop(priorityQueue)
        heapq.heappop(priorityQueueForNode)
        path = path + [i]
        start=i
    return  path


graph = {'A': {'B':2, 'C':5},
     'B': {'C':2, 'D':5},
     'C': {'D':4, 'G':2},
     'D': {'C':6, 'E':4},
     'E': {'F':1},
     'F':{'K':3,'L':4}

  }

print(Hill_Climbing('A',graph))  # this first code