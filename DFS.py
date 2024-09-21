def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set if not provided

    # Mark the current node as visited
    visited.add(start)
    print(start)  # Print or process the node

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited  # Optional: return visited nodes

# Example usage:
if __name__ == "__main__":
    # Representing a graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_vertex = 'A'
    print("DFS traversal starting from vertex A:")
    dfs(graph, start_vertex)
