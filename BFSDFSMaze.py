from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])  # Add starting element to queue
    visited = set()  # Create a set
    visited.add(start)  # Add starting element to set
    parent = {start: None}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], nodes_explored

        row, col = current
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1 and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.add((nr, nc))
                parent[(nr, nc)] = current

    return None, nodes_explored  # If no path is found

def dfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    stack = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}
    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], nodes_explored

        row, col = current
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1 and (nr, nc) not in visited:
                stack.append((nr, nc))
                visited.add((nr, nc))
                parent[(nr, nc)] = current

    return None, nodes_explored  # No path found


# Example usage
if __name__ == "__main__":
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    start = (0, 0)
    end = (4, 4)

    bfs_path, bfs_nodes = bfs(maze, start, end)
    dfs_path, dfs_nodes = dfs(maze, start, end)

    print("BFS:")
    print(f"Path: {bfs_path}")
    print(f"Nodes Explored: {bfs_nodes}")

    print("\nDFS:")
    print(f"Path: {dfs_path}")
    print(f"Nodes Explored: {dfs_nodes}")
