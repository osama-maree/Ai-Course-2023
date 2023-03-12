

def dfs(graph,goal):
    root = list(graph.keys())[0]
    stack, temp, path, visited = [root], [], [], []  #the temp list for add child current node to stack,path this is solution
    parent = {root: None}
    while stack:
        v = stack.pop()                #take last item inserted stack
        if v == goal:                  #check if this is goal
            while parent[goal]:
                path.insert(0, goal)
                goal = parent[goal]
            path.insert(0, root)
            break
        visited.append(v)        #add current node to visited node
        for i in graph[v]:
            if i not in visited:

            temp.append(i)
            parent[i] = v
        while temp:
            stack.append(temp.pop())
    return path


graph ={1:[2,3] ,2:[5,6],3:[7,8],4:[],5:[9],6:[2,5],7:[2,4],8:[1],9:[]} #direction graph
goal = 7
print(dfs(graph, goal))
