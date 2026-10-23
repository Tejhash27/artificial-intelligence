from collections import deque

def get_neighbors(state):
    """Generates all valid next states by moving the blank tile (0)."""
    neighbors = []
    # Find the position of the blank tile (0)
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    
    # Define possible movements: (row_change, col_change)
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    
    for move, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        
        # Check if the move stays within the 3x3 board boundaries
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            
            # Convert tuple to list to swap tiles, then convert back
            state_list = list(state)
            state_list[blank_idx], state_list[new_blank_idx] = state_list[new_blank_idx], state_list[blank_idx]
            neighbors.append((tuple(state_list), move))
            
    return neighbors

def solve_8_puzzle(start_state, goal_state):
    """Solves the 8-puzzle using Breadth-First Search (BFS)."""
    # Queue stores: (current_state, path_taken_to_reach_it)
    queue = deque([(start_state, [])])
    visited = {start_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check if we have reached the goal configuration
        if current_state == goal_state:
            return path
            
        # Explore valid moves
        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [move]))
                
    return None  # Return None if the puzzle is unsolvable

# --- Example Usage ---
if __name__ == "__main__":
    # Define the 3x3 grid as a flat tuple (0 represents the blank space)
    # Grid equivalent:
    # 1 2 3
    # 0 4 6
    # 7 5 8
    start = (1, 2, 3, 
             0, 4, 6, 
             7, 5, 8)
             
    goal  = (1, 2, 3, 
             4, 5, 6, 
             7, 8, 0)

    print("Searching for a solution...")
    solution_path = solve_8_puzzle(start, goal)
    
    if solution_path is not None:
        print(f"Success! Solved in {len(solution_path)} moves.")
        print("Sequence of moves:", " -> ".join(solution_path))
    else:
        print("No solution exists for this configuration.")
