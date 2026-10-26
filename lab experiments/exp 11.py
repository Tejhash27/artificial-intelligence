def is_safe(region, color, assignment, graph):
    """Checks if it's legal to assign this color to the current region."""
    # Check every neighbor of the current region
    for neighbor in graph[region]:
        # If a neighbor already has this color, it's an invalid assignment
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack_map_coloring(regions, colors, assignment, graph):
    """Core CSP Backtracking algorithm to find a valid color assignment."""
    # Base case: If all regions have a color assigned, we are done!
    if len(assignment) == len(regions):
        return assignment

    # Select the next unassigned region (Variables)
    # We take the first region that doesn't exist in our assignment dictionary yet
    current_region = [r for r in regions if r not in assignment][0]

    # Try assigning each available color (Domain Values)
    for color in colors:
        if is_safe(current_region, color, assignment, graph):
            # Assign the color (Forward step)
            assignment[current_region] = color

            # Recursively try to color the rest of the map
            result = backtrack_map_coloring(regions, colors, assignment, graph)
            if result is not None:
                return result

            # If it leads to a dead end, undo the assignment (Backtrack step)
            del assignment[current_region]

    return None  # Return None if no valid coloring exists with these colors


# --- Execution Example ---
if __name__ == "__main__":
    # 1. Variables: The regions/states to be colored
    map_regions = ["A", "B", "C", "D", "E"]

    # 2. Domains: The available colors
    available_colors = ["Red", "Green", "Blue"]

    # 3. Constraints: An Adjacency List representing bordering regions
    # (e.g., Region A borders B, C, and D)
    map_graph = {
        "A": ["B", "C", "D"],
        "B": ["A", "C", "E"],
        "C": ["A", "B", "D", "E"],
        "D": ["A", "C", "E"],
        "E": ["B", "C", "D"]
    }

    # Run the CSP solver starting with an empty assignment dictionary
    solution = backtrack_map_coloring(map_regions, available_colors, {}, map_graph)

    print("--- CSP Map Coloring Solution ---")
    if solution:
        for region, color in sorted(solution.items()):
            print(f"Region {region} -> Color: {color}")
    else:
        print("No valid solution found with the provided colors.")
