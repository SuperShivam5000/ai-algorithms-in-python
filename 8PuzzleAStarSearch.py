from heapq import heappop, heappush
import numpy as np

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
dirs = {'U': -3, 'D': 3, 'L': -1, 'R': 1}

# Heuristic 1: Number of misplaced tiles
def h1(state):
    return sum(1 for i in range(9) if state[i] and state[i] != goal_state[i])

# Heuristic 2: Manhattan distance
def h2(state):
    return sum(abs(i // 3 - state[i] // 3) + abs(i % 3 - state[i] % 3)
               for i in range(9) if state[i])

def get_neighbors(state):
    zero_idx = state.index(0)
    neighbors = []
    for move, delta in dirs.items():
        new_idx = zero_idx + delta
        if 0 <= new_idx < 9 and not (zero_idx % 3 == 2 and move == 'L') and not (zero_idx % 3 == 0 and move == 'R'):
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))
    return neighbors

def astar(start, heuristic):
    pq, visited = [(heuristic(start), 0, start, [])], set()
    while pq:
        _, cost, state, path = heappop(pq)
        if state in visited: continue
        visited.add(state)
        if state == goal_state: return path
        for neighbor in get_neighbors(state):
            heappush(pq, (cost + heuristic(neighbor) + 1, cost + 1, neighbor, path + [neighbor]))
    return None

start_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)
print("Solution using H1:", astar(start_state, h1))
print("Solution using H2:", astar(start_state, h2))
