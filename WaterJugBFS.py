from collections import deque

def water_jug_bfs(start,goal,capacity):
    queue=deque()
    queue.append(start)
    parent={}
    parent[start] = None

    while queue:
        f = queue.popleft()

        if f == goal:
            return reconstruct_path(parent, start, goal)
        
        a = (f[0], 0)
        b = (0, f[1])
        c = (min(capacity[0], f[0] + f[1]), max(0, f[0] + f[1] - capacity[0]))
        d = (max(0, f[0] + f[1] - capacity[1]), min(capacity[1], f[0] + f[1]))
        e = (capacity[0], f[1])
        f_new = (f[0], capacity[1])
        
        for state in [a, b, c, d, e, f_new]:
            if state not in parent:
                parent[state] = f
                queue.append(state)

    return None

def reconstruct_path(parent,start,goal):
    if goal not in parent: 
        return None

    path=[]
    state=goal
    while state is not None:
        path.append(state)
        state=parent[state]
    return path[::-1]

start_state=(0,0)
goal_state=(0,4)
capacity=(3,5)
solution=water_jug_bfs(start_state,goal_state,capacity)
print("Path: ",solution)