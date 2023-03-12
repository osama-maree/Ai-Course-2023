def dfs(root,goal,graph,visited):
    visited.append(root)
    if root == goal:
        return  [root]
    for i in graph.get(root,[]):
        if i not in visited:
            path = dfs(i,goal,graph,visited)
            if path:
                return [root] + path

    return  []


graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[1]} #direction graph
goal = 5
visited=[]
print(dfs(list(graph.keys())[0],goal,graph,visited))
