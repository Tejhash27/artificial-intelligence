from collections import deque

class Graph:
    def __init__(self):
        # Use a dictionary to store the adjacency list
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

    def bfs(self, start_node):
        """Performs BFS traversal from a given start node."""
        if start_node not in self.graph:
            print(f"❌ Start node '{start_node}' not found in the graph.")
            return []

        # Queue for keeping track of nodes to visit (FIFO)
        queue = deque([start_node])
        
        # Set to track visited nodes to prevent cycles and infinite loops
        visited = set([start_node])
        
        # List to store the order of traversal
        traversal_order = []

        print(f"🔄 Starting BFS Traversal from node: {start_node}")
        
        while queue:
            # Dequeue a vertex from the front of the queue
            current_node = queue.popleft()
            traversal_order.append(current_node)
            
            # Get all adjacent vertices of the dequeued vertex.
            # If an adjacent vertex has not been visited, mark it visited and enqueue it.
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
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

    # Execute BFS starting from node 'A'
    result = g.bfs('A')
    
    print("\n✅ BFS Traversal Path:")
    print(" -> ".join(result))
