import  heapq
def Hill_Climbing(start,graph):
    path,prevNode =[start], [10, start]
    while 1 :
        d=graph.get(start,[])
        priorityQueue=[]
        if d:
            for i in d:
                heapq.heappush(priorityQueue,(d[i],i))
            (cost, i) = heapq.heappop(priorityQueue)
            if prevNode[0] >= cost:
                path = path+ [i]
                prevNode=[cost,i]
                start=i
            else:
                return  path
        else:
            return path


graph = {'A': {'B':2, 'C':5},# this is heur not Gn
     'B': {'C':2, 'D':5},
     'C': {'D':4, 'G':2},
     'D': {'C':6, 'E':4},
     'E': {'F':1},
     'F':{'K':3,'L':4}

  }
print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
print(Hill_Climbing('A',graph))  # this first code