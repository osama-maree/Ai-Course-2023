def dfs(graph,goal):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [root], [], [], []
    parent = {root: None}
    while stack:
        v = stack.pop()
        visited.append(v)
        if v == goal:
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break
        for i in graph.get(v,[]):
            if i not in visited:
                 temp.append(i)
                 parent[i] = v
        while temp:
            stack.append(temp.pop())
    return path,visited

print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[1]} #direction graph
path,visited=dfs(graph, 7)
print("found goal  path :",path,"and visited node :",visited,sep=" ",end="*^^*")








