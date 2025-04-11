from collections import deque

def construct_path(meeting_point,parent_start,parent_end):
    path=[]
    node=meeting_point
    while(node is not None):
        path.append(node)
        node=parent_start[node]
    path.reverse()
    path.pop()

    node=meeting_point
    while(node is not None):
        path.append(node)
        node=parent_end[node]
    return path


def bidirectional_bfs(graph,start,end):
    if start==end: return [start]

    queue_start=deque([start])
    queue_end=deque([end])
    visited_start={start}
    visited_end={end}
    parent_start={start: None}
    parent_end={end: None}

    while queue_start and queue_end:
        for _ in range(len(queue_start)):
            current_start=queue_start.popleft()
            for neighbor in graph[current_start]:
                if(neighbor not in visited_start):
                    visited_start.add(neighbor)
                    parent_start[neighbor]=current_start
                    queue_start.append(neighbor)
                    if neighbor in visited_end:
                        return construct_path(neighbor,parent_start,parent_end)
        
        for _ in range(len(queue_end)):
            current_end=queue_end.popleft()
            for neighbor in graph[current_end]:
                if neighbor not in visited_end:
                    visited_end.add(neighbor)
                    parent_end[neighbor]=current_end
                    queue_end.append(neighbor)
                    if neighbor in visited_start:
                        return construct_path(neighbor,parent_start,parent_end)
    
    return None


#adjacency list
city_map = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"]
    }

start_location = "A"
end_location = "G"
shortest_path = bidirectional_bfs(city_map, start_location, end_location)
print(shortest_path)