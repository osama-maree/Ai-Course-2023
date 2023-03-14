def dfs(root,goal,graph,visited,path):
    if root in visited:
        return
    visited.append(root)
    if root == goal:
        path.append(goal)
        return path
    for i in graph.get(root,[]):
            if dfs(i,goal,graph,visited,path):
                path.insert(0,root)
                return path

    return path


graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[1]} #direction graph
goal = 4
visited, path = [], []
print(dfs(list(graph.keys())[0],goal,graph,visited,path))
