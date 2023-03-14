def bfs(graph,goal):
    root = list(graph.keys())[0]
    queue, temp, path, visited = [root], [], [], []
    parent = {root: None}
    while queue:
        v = queue.pop(0)
        if v == goal:
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break
        visited.append(v)
        for i in graph.get(v,[]):
            if i not in visited:
                 queue.append(i)
                 parent[i] = v
    return path,visited


graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[1]} #direction graph
goal = 7
path,visited=bfs(graph, goal)
if path:
    print("found goal  path :",path,"and visited node :",visited,sep=" ",end="*^^*")
else:
    print("goal not found")
