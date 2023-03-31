def bfs(graph,goal):
    root = list(graph.keys())[0]
    queue, temp, path, visited = [root], [], [], []
    parent = {root: None}
    while queue:
        v = queue.pop(0)
        if v in visited:
            continue
        visited.append(v)
        if v == goal:
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break
        for i in graph.get(v,[]):
                 queue.append(i)
                 parent[i] = v
    return path,visited

print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[1]} #direction graph
goal = 7
path,visited=bfs(graph, goal)
if path:
    print("found goal  path :",path,"and visited node :",visited,sep=" ",end="*^^*")
else:
    print("goal not found")
