"""
CIS 365 Artificial Intelligence

This is a simple Breadth First Search and Depth First Search program.
"""

""" Breadth First Search of a graph from starting node to ending node """
def bfs(graph, start, end):

    # List that contains the nodes that have already been inspected, initially empty
    visited = list()

    # List that contains the next nodes to be inspected, implemented as FIFO
    queue = [start]

    # Run until queue is empty or end is found
    while queue:

        # Take the first item from queue
        node = queue.pop(0)

        # Add current node to visited if not already in visited
        if node not in visited:
            visited.append(node)

        # Return the visited list if at the end
        if node == end:
            return visited
        else:
            # Otherwise add the nodes children to end of queue
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)

    return visited

""" Depth First Search of a graph from starting node to ending node """
def dfs(graph, start, end):

    # List that contains the nodes that have already been inspected, initially empty
    visited = list()

    # List that contains the next nodes to be inspected, implemented as LIFO
    stack = [start]

    # Run until stack is empty or end is found
    while stack:

        i = 0

        # Take the first item from stack
        node = stack.pop(0)

        # Add current node to visited if not already in visited
        if node not in visited:
            visited.append(node)

        # Return the visited list if at the end
        if node == end:
            return visited
        else:
            # Otherwise add the nodes children to stack according to its spot
            for child in graph[node]:
                if child not in visited:
                    stack.insert(i, child)
                    i += 1

    return visited

"""Start program"""
if __name__ == '__main__':

    # Labeled maze as a graph
    # node edges were ordered to search for path from Left, Up, Right then Down
    graph = {
        'A' : ['F'],
        'B' : ['M'],
        'C' : ['E'],
        'D' : ['F'],
        'E' : ['C', 'F', 'G'],
        'F' : ['E','D', 'A'],
        'G' : ['H', 'E', 'I'],
        'H' : ['G'],
        'I' : ['G', 'K', 'L'],
        'J' : ['L'],
        'K' : ['I'],
        'L' : ['J', 'I', 'M'],
        'M' : ['L', 'B']
    }

    start = 'M'
    end = "A"

    # Breadth first search from starting node to ending node
    bfs_list = bfs(graph, start, end)
    print("\nThe Breadth First Search path from", start, "to", end, ":", bfs_list)

    # Depth first search from starting node to ending node
    dfs_list = dfs(graph, start, end)
    print("\nThe Depth First Search path from", start, "to", end, ":", dfs_list)



