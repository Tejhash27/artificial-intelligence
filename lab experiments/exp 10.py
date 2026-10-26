import heapq

class Node:
    """Represents a coordinate point on the grid map."""
    def __init__(self, position, parent=None):
        self.position = position  # (row, col) tuple
        self.parent = parent      # Keeps track of the path back to start
        
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost (estimated distance to goal)
        self.f = 0  # Total estimated cost (g + h)

    def __lt__(self, other):
        """Allows nodes to be sorted inside the priority queue based on f-cost."""
        return self.f < other.f

def manhattan_distance(pos1, pos2):
    """Calculates the grid-based heuristic distance."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def astar(grid, start, end):
    """Executes the A* pathfinding algorithm on a 2D grid matrix."""
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # Initialize start and end nodes
    start_node = Node(start)
    end_node = Node(end)
    
    # Priority queue tracking nodes to visit (Open List)
    open_list = []
    # Track coordinates already processed (Closed List)
    closed_set = set()
    
    # Add start node to priority queue
    heapq.heappush(open_list, start_node)
    
    # Track the lowest g-cost for each position to prevent revisiting worse paths
    g_scores = {start: 0}
    
    # Movement directions (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_list:
        # Get the node with the lowest total estimated cost (f)
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position
        
        # If we reached the goal, reconstruct and return the path
        if current_pos == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path (start to end)
            
        closed_set.add(current_pos)
        
        # Explore adjacent neighbor squares
        for r_move, c_move in directions:
            neighbor_pos = (current_pos[0] + r_move, current_pos[1] + c_move)
            
            # Check map boundaries
            if not (0 <= neighbor_pos[0] < num_rows and 0 <= neighbor_pos[1] < num_cols):
                continue
                
            # Check for obstacles (1 represents a wall)
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue
                
            # Skip if we have already finalised this coordinate
            if neighbor_pos in closed_set:
                continue
                
            # Calculate tentative g-cost (moving 1 step costs 1 unit)
            tentative_g = current_node.g + 1
            
            # If this path to neighbor is better than any previous one, record it
            if tentative_g < g_scores.get(neighbor_pos, float('inf')):
                g_scores[neighbor_pos] = tentative_g
                
                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = tentative_g
                neighbor_node.h = manhattan_distance(neighbor_pos, end_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                
                heapq.heappush(open_list, neighbor_node)
                
    return None  # No path found

# --- Execution Example ---
if __name__ == "__main__":
    # 0 = Empty printable space, 1 = Wall/Obstacle
    grid_map = [,
 ,
 ,
 ,
        [0, 0, 0, 0, 0]
    ]
    
    start_point = (0, 0)  # Top-left corner
    end_point = (4, 4)    # Bottom-right corner
    
    shortest_path = astar(grid_map, start_point, end_point)
    
    print("--- A* Search Algorithm Results ---")
    if shortest_path:
        print(f"Path Found ({len(shortest_path)} steps): {shortest_path}\n")
        
        # Visualise path on the map grid
        for r in range(len(grid_map)):
            row_display = []
            for c in range(len(grid_map[0])):
                if (r, c) == start_point:
                    row_display.append("S")  # Start
                elif (r, c) == end_point:
                    row_display.append("E")  # End
                elif (r, c) in shortest_path:
                    row_display.append("•")  # Path Taken
                elif grid_map[r][c] == 1:
                    row_display.append("█")  # Obstacle Wall
                else:
                    row_display.append(" ")  # Open Space
            print(" ".join(row_display))
    else:
        print("No route exists to the destination.")
