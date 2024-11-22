import numpy as np

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank space
]

# Heuristic: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            neighbor = [row[:] for row in state]
            neighbor[x][y], neighbor[nx][ny] = neighbor[nx][ny], neighbor[x][y]
            neighbors.append(neighbor)
    return neighbors

# Hill Climbing Algorithm
def hill_climbing(initial_state):
    current_state = initial_state
    current_cost = manhattan_distance(current_state)
    
    while True:
        neighbors = get_neighbors(current_state)
        neighbor_costs = [(manhattan_distance(neighbor), neighbor) for neighbor in neighbors]
        best_cost, best_neighbor = min(neighbor_costs, key=lambda x: x[0])
        
        if best_cost >= current_cost:  # No better neighbor
            break
        
        current_state = best_neighbor
        current_cost = best_cost
    
    return current_state, current_cost

# Test the implementation
initial_state = [
    [1, 2, 3],
    [4, 5, 0],
    [7, 8, 6]
]

final_state, final_cost = hill_climbing(initial_state)
print("Final State:")
for row in final_state:
    print(row)
print(f"Cost: {final_cost}")
