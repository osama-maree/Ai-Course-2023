import heapq
def uniform_cost_search(start, goal, graph):
    visited = set()
    heap = [(0, start, [])]
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        print(path)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return (cost, path)

            for i in graph[node]:
                if i not in visited:
                    total_cost = cost + graph[node][i]
                    heapq.heappush(heap, (total_cost, i, path))

    return None
hgraph = {'A': {'B':2, 'C':3},
     'B': {'C':2, 'D':5},
     'C': {'D':4, 'G':2},
     'D': {'C':6, 'E':4},
     'E': {'F':1},
     'F': [],
     'G': []}
print(uniform_cost_search('A','F', hgraph))

# print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
# graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[10]} #direction graph
# goal,maxD = 2,5
#
# for i in range(1,maxD):
#     path,visited = dfs(graph,goal,i)
#     if path:
#         print("found goal in level :",i,"and path :",path,"and visited node :",visited,sep=" ",end="*^^*")
#         break
# else:
#     print("goal not found")






