import sys

def tsp_held_karp(distance_matrix):
    n = len(distance_matrix)
    
    # Memoization table: maps (current_node, visited_mask) -> (min_distance, path)
    memo = {}

    def visit(mask, current):
        # Base Case: All cities have been visited (mask has all 1s)
        # Return the distance from the current city back to the starting city (0)
        if mask == (1 << n) - 1:
            return distance_matrix[current][0], [0]

        # Check if this state has already been calculated
        if (mask, current) in memo:
            return memo[(mask, current)]

        min_dist = sys.maxsize
        best_path = []

        # Try visiting all other unvisited cities
        for next_city in range(n):
            # Check if next_city has not been visited yet
            if not (mask & (1 << next_city)):
                # Calculate the sub-problem distance and path
                new_mask = mask | (1 << next_city)
                sub_dist, sub_path = visit(new_mask, next_city)
                
                total_dist = distance_matrix[current][next_city] + sub_dist
                
                # If this is the shortest path found so far, update
                if total_dist < min_dist:
                    min_dist = total_dist
                    best_path = [next_city] + sub_path

        # Cache the result in the memoization table
        memo[(mask, current)] = (min_dist, best_path)
        return min_dist, best_path

    # Start from city 0, with only city 0 marked as visited (mask = 1)
    initial_mask = 1
    optimal_cost, sequence = visit(initial_mask, 0)
    
    # Complete the path by adding the starting city at the beginning
    full_path = [0] + sequence
    
    return optimal_cost, full_path


# --- Execution Example ---
if __name__ == "__main__":
    # Define a distance matrix representing 4 cities (0, 1, 2, 3)
    cities = ["City A", "City B", "City C", "City D"]
    
    graph = [,
 ,
 ,
        [20, 25, 30, 0]
    ]

    cost, path_indices = tsp_held_karp(graph)
    
    # Translate numeric indices back to readable city names
    readable_path = [cities[idx] for idx in path_indices]

    print("=========================================")
    print("      TRAVELLING SALESMAN PROBLEM        ")
    print("=========================================\n")
    print(f"✅ Minimum/Optimal Cost: {cost}")
    print(f"🛣️  Optimal Route Strategy:\n    " + " -> ".join(readable_path))
