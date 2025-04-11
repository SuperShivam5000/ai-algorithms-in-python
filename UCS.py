import heapq

#UCS
def uniform_cost_search(graph,start,goal):
    priority_queue=[(0,start,[])]
    visited=set()

    while priority_queue:
        cost,current_node,path=heapq.heappop(priority_queue)
        if current_node in visited: continue #skip visited nodes
        visited.add(current_node)
        path=path+[current_node]
        if(current_node==goal): return cost,path

        for neighbour,weight in graph.get(current_node,[]):
            if neighbour not in visited: heapq.heappush(priority_queue,(cost+weight,neighbour,path))
    
    return float("inf"),[] #return infinity

#define adjacency list
graph={
    'A':[('B',1),('C',4)],
    'B':[('A',1),('C',2),('D',5)],
    'C':[('A',4),('B',2),('D',1)],
    'D':[('B',5),('C',1)]
}

start,goal='A','D'
ucs_cost,ucs_path=uniform_cost_search(graph,start,goal)
print("Cost: ", ucs_cost)
print("Path: ", ucs_path)
