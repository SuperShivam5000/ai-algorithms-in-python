import time
from collections import deque

def is_valid_state(state):
    """Check if the given state is valid."""
    return state is not None

def find_empty(state):
    """Find the index of the empty space (0) in the 1D array."""
    return state.index(0)

def generate_successors(state):
    """Generate all possible successor states from the given state."""
    successors = []
    empty_idx = find_empty(state)
    row, col = divmod(empty_idx, 3)
    
    # Define possible moves: (row_offset, col_offset)
    moves = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1)
    }

    for direction, (row_offset, col_offset) in moves.items():
        new_row, new_col = row + row_offset, col + col_offset
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = state[:]
            # Swap empty space with the target tile
            new_state[empty_idx], new_state[new_idx] = new_state[new_idx], new_state[empty_idx]
            successors.append((new_state, direction))

    return successors

def bfs(initial_state, goal_state):
    """Breadth-First Search implementation."""
    queue = deque([(initial_state, [])])  # (state, path)
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if tuple(current_state) in visited:
            continue

        visited.add(tuple(current_state))

        if current_state == goal_state:
            return path, len(visited)

        for successor, direction in generate_successors(current_state):
            if tuple(successor) not in visited:
                queue.append((successor, path + [direction]))

    return None, len(visited)

def dfs(initial_state, goal_state):
    """Depth-First Search implementation."""
    stack = [(initial_state, [])]  # (state, path)
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if tuple(current_state) in visited:
            continue

        visited.add(tuple(current_state))

        if current_state == goal_state:
            return path, len(visited)

        for successor, direction in generate_successors(current_state):
            if tuple(successor) not in visited:
                stack.append((successor, path + [direction]))

    return None, len(visited)

def main():
    # Define initial and goal states
    initial_state = [1, 2, 3, 4, 0, 5, 7, 8, 6]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # Solve using BFS
    start_time = time.time()
    bfs_result, bfs_explored = bfs(initial_state, goal_state)
    bfs_time = time.time() - start_time

    print("BFS Result:")
    print(f"Path to Goal: {' -> '.join(bfs_result) if bfs_result else 'No solution'}")
    print(f"Number of Moves: {len(bfs_result) if bfs_result else 0}")
    print(f"Execution Time: {bfs_time:.4f} seconds")
    print(f"Nodes Explored: {bfs_explored}")

    # Solve using DFS
    start_time = time.time()
    dfs_result, dfs_explored = dfs(initial_state, goal_state)
    dfs_time = time.time() - start_time

    print("\nDFS Result:")
    print(f"Path to Goal: {' -> '.join(dfs_result) if dfs_result else 'No solution'}")
    print(f"Number of Moves: {len(dfs_result) if dfs_result else 0}")
    print(f"Execution Time: {dfs_time:.4f} seconds")
    print(f"Nodes Explored: {dfs_explored}")

if __name__ == "__main__":
    main()
