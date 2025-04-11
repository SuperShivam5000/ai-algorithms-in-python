import heapq

def manhattan_distance(start,treasure):
    x1,y1=start
    x2,y2=treasure
    distance=abs(x1-x2)+abs(y1-y2)
    return distance

def get_neighbors(current,row,col):
    x,y=current
    neighbors=[]
    if 0<=x-1: neighbors.append((x-1,y))
    if x<row: neighbors.append((x+1,y))
    if 0<=y-1: neighbors.append((x,y-1))
    if y<col: neighbors.append((x,y+1))
    return neighbors

def reconstruct_path(parent,start,treasure):
    path=[]
    current=treasure
    while(current!=start):
        path.append(current)
        current=parent[current]
    path.append(start)
    path.reverse()
    return path

def best_first_search(grid,start,treasure):
    row=len(grid)
    col=len(grid[0])
    visited=set()
    pq=[]
    parent={}

    heapq.heappush(pq,(manhattan_distance(start,treasure),start))
    
    while pq:
        _,current=heapq.heappop(pq)
        visited.add(current)
        if current==treasure: return reconstruct_path(parent,start,treasure)

        #get neighbours
        neighborarray = get_neighbors(current,row,col)
        for neighbor in neighborarray:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=current
                heapq.heappush(pq,(manhattan_distance(neighbor,treasure),neighbor))
    return None            

#execution
grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
start=(0,0)
treasure=(3,3)
path=best_first_search(grid,start,treasure)
print("Path: ",path)