class Graph:
    def __init__(self):
        # Dictionary to store the adjacency list
        self.graph = {}

    def add_edge(self, u, v, bidirectional=True):
        """Adds an edge between vertex u and vertex v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
            
        self.graph[u].append(v)
        if bidirectional:
            self.graph[v].append(u)

    def dfs_recursive(self, start_node):
        """Wrapper method for recursive DFS traversal."""
        if start_node not in self.graph:
            print(f"❌ Start node '{start_node}' not found in the graph.")
            return []
            
        visited = set()
        traversal_order = []
        
        def _dfs_util(node):
            # Mark the current node as visited and save it
            visited.add(node)
            traversal_order.append(node)
            
            # Recur for all vertices adjacent to this vertex
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    _dfs_util(neighbor)
                    
        _dfs_util(start_node)
        return traversal_order

    def dfs_iterative(self, start_node):
        """Performs DFS traversal using an explicit stack."""
        if start_node not in self.graph:
            return []

        stack = [start_node]
        visited = set()
        traversal_order = []

        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                
                # Push all unvisited neighbors to the stack.
                # Reversed order matches standard recursive output hierarchy.
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        
        return traversal_order


# --- Execution Example ---
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    
    # Building a sample tree/graph structure:
    #      A
    #     / \
    #    B   C
    #   / \   \
    #  D   E   F
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    # Execute Recursive DFS starting from node 'A'
    recursive_result = g.dfs_recursive('A')
    print("✅ DFS Traversal Path (Recursive):")
    print(" -> ".join(recursive_result))
    
    # Execute Iterative DFS starting from node 'A'
    iterative_result = g.dfs_iterative('A')
    print("\n✅ DFS Traversal Path (Iterative):")
    print(" -> ".join(iterative_result))
