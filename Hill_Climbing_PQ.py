


def Hill_Climbing(graph,start,heuristic):
    path,PrevNode=[start],[heuristic[start],start]
    while 1:
       child=graph.get(start,[])
       PQ=[]
       if child:
           for i in child:
               PQ=PQ+[(heuristic[i],i)]
           PQ.sort()
           (H,node)=PQ.pop(0)
           if H <= PrevNode[0]:
               path=path+[node]
               PrevNode=[H,node]
               start=node
           else:
               return path
       else:
           return path

graph = {'A': {'B', 'C'},
     'B': {'C', 'D'},
     'C': {'D', 'G'},
     'D': {'C', 'E'},
     'E': {'F','J'},
     'F':{'K','L'}

  }
heuristic={
    'A':12,
    'K':10,
    'C':11,
    'B':10,
    'E':7,
    'G':6,
    'F':5,
    'L':2,
    'D':11,
    'J':6

}
print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
path = Hill_Climbing(graph,'A',heuristic)
if path:
    print("found Solution :",path)
else:
    print("error message")
