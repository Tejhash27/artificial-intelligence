class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        """
        Initializes the CSP environment.
        :param variables: List of regions (e.g., ['WA', 'NT', 'SA'])
        :param domains: Dictionary mapping regions to available colors {region: [colors]}
        :param neighbors: Dictionary mapping regions to adjacent regions {region: [neighbors]}
        """
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.assignments = {}

    def is_consistent(self, variable, color):
        """Checks if assigning a color to a variable violates any constraints."""
        for neighbor in self.neighbors.get(variable, []):
            if neighbor in self.assignments and self.assignments[neighbor] == color:
                return False
        return True

    def get_mrv_variable(self):
        """Minimum Remaining Values (MRV) Heuristic: Picks the unassigned variable with the fewest choices left."""
        unassigned = [v for v in self.variables if v not in self.assignments]
        # Sort by the number of legal colors remaining in their domain
        return min(unassigned, key=lambda v: len(self.domains[v]))

    def forward_check(self, variable, color):
        """
        Looks ahead to neighbors and removes the chosen color from their domain.
        Returns a dictionary of pruned options to restore if backtracking is needed.
        """
        pruned = {}
        for neighbor in self.neighbors.get(variable, []):
            if neighbor not in self.assignments and color in self.domains[neighbor]:
                if len(self.domains[neighbor]) == 1:
                    # Pointless to proceed if a neighbor is left with 0 choices
                    return None 
                self.domains[neighbor].remove(color)
                pruned[neighbor] = color
        return pruned

    def restore_domains(self, pruned):
        """Restores domains back to their original state during backtracking."""
        for neighbor, color in pruned.items():
            self.domains[neighbor].append(color)

    def backtrack_search(self):
        """Core recursive backtracking algorithm."""
        # Base Case: All variables successfully assigned
        if len(self.assignments) == len(self.variables):
            return self.assignments

        # 1. Select the next variable using MRV
        var = self.get_mrv_variable()

        # 2. Iterate through all available values (colors) in its domain
        for color in list(self.domains[var]):
            if self.is_consistent(var, color):
                # Make assignment
                self.assignments[var] = color
                
                # 3. Apply Forward Checking
                pruned = self.forward_check(var, color)
                
                if pruned is not None:
                    # Recursively solve the remaining variables
                    result = self.backtrack_search()
                    if result is not None:
                        return result
                    
                    # Backtrack forward checking if it failed down the line
                    self.restore_domains(pruned)

                # Backtrack assignment
                del self.assignments[var]

        return None # Return None if no solution exists in this branch


# --- Example Usage (Classical Australia Map Colouring Problem) ---
if __name__ == "__main__":
    # States (Variables)
    states = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']

    # Available Colors (Domains) - Map can be colored using 3 distinct colors
    colors = ['Red', 'Green', 'Blue']
    state_domains = {state: list(colors) for state in states}

    # Adjacency constraints (Neighbors)
    map_neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q':  ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V':  ['SA', 'NSW'],
        'T':  []  # Tasmania has no neighbors
    }

    # Instantiate and execute the CSP solver
    csp = MapColoringCSP(states, state_domains, map_neighbors)
    solution = csp.backtrack_search()

    # Display results
    print("--- Map Colouring CSP Solution ---")
    if solution:
        for state, color in sorted(solution.items()):
            print(f"{state:4} : {color}")
    else:
        print("No valid coloring scheme exists with the provided colors.")
