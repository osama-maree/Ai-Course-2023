def dfs(root,goal,graph,visited,path,limit):
    if limit > 0:
        if root in visited:
            return
        visited.append(root)
        if root == goal:
            path.append(goal)
            return path
        for i in graph.get(root,[]):
                if dfs(i,goal,graph,visited,path,limit-1):
                    path.insert(0,root)
                    return path

        return path

print("*"*80,"\n\t\t\t\t\t\t\tOsama Maree\n","*"*80)
graph ={1:[2,3] ,2:[5,6],3:[7,8],5:[9],6:[2,5],7:[2,4],8:[1]} #direction graph
goal = 7
visited, path = [], []
maxD=4
for i in range(1,maxD):
    path = dfs(list(graph.keys())[0],goal,graph,visited,path,i)
    if path:
        print("found goal in level :",i,"and path :",path,"and visited node :",visited,sep=" ",end="*^^*")
        break
    path,visited=[],[]
else:
    print("goal not found")