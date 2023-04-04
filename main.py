def dfs(g, goal2):
    goal = goal2
    root = list(g.keys())[0]
    stack, temp, visited = [root], [], []
    path = []  # path for Solution from start to goal node
    childpar = {root: None}

    while stack:
        node = stack.pop()

        # print(node,end=" ")  you can print all the node that traverse from start to goal

        if node == goal:
            path.append(goal)
            while goal != 1:
                path.insert(0, childpar[goal])  # add in the fisrt of the path list
                goal = childpar[goal]
            print(path)
            path = []
            goal = goal2


        if node in visited:
            continue
        visited.append(node)

        for i in g.get(node, []):  # i=children   node=parent  (child:parent)
            temp.append(i)
            childpar[i] = node

        while temp:
            stack.append(temp.pop())
            #  print(path)


g = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [4, 11], 6: [12, 13], 7: [14, 15]}
goal = 4
dfs(g,goal) #call function