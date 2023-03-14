def dfs(graph,goal,limit):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [(root,1)], [], [], []
    parent = {root: None}
    while stack:
        v,d = stack.pop()
        if v == goal:
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break
        visited.append(v)
        for i in graph.get(v,[]):
            if i not in visited and d < limit:
                 temp.append(i)
                 parent[i] = v
        while temp:
            stack.append((temp.pop(),d+1))
    return path,visited


graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[10]} #direction graph
goal,maxD = 2,5

for i in range(1,maxD):
    path,visited = dfs(graph,goal,i)
    if path:
        print("found goal in level :",i,"and path :",path,"and visited node :",visited,sep=" ",end="*^^*")
        break
else:
    print("goal not found")






