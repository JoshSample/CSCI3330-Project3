"""
Josh Sample, Jack Thurber, Anthony Sweeney
CSCI 3330
11/3/2019
"""
import networkx as nx  # This is the graph ADT we are working with


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))


def bfs_path(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def problem_1(graph):
    # Instantiate G1 as a graph object
    G1 = nx.Graph()
    # Add graph edges to G1 object
    for k, v in graph.items():
        for vv in v:
            G1.add_edge(k, vv)
    # Problem 1
    print("DFS:", list(nx.dfs_edges(G1, 'a')))
    print("DFS with other remaining edges:", list(nx.dfs_edges(G1, 'h')))
    print("BFS:", list(nx.bfs_edges(G1, 'a')))
    print("BFS with other remaining edges:", list(nx.bfs_edges(G1, 'h')))


def problem_3():
    # G2 is another networkx object
    G2 = nx.DiGraph()
    # Create the graph in problem 3
    G2.add_edges_from([(1, 3), (3, 5), (3, 2), (2, 1), (4, 1),
                       (4, 2), (4, 12), (11, 12), (5, 6), (5, 8),
                       (6, 8), (6, 7), (6, 10), (10, 9), (8, 9),
                       (8, 10), (7, 10), (10, 11)])
    # Print out strongly connected components
    print("Strongly connected points of the DAG:",
          list(nx.strongly_connected_components(G2)))


def problem_4():
    # G3 is problem 4's object
    G3 = nx.Graph()
    # Add weighted edges
    G3.add_edge('A', 'C', weight=9)
    G3.add_edge('A', 'B', weight=22)
    G3.add_edge('A', 'D', weight=12)
    G3.add_edge('B', 'C', weight=35)
    G3.add_edge('C', 'D', weight=4)
    G3.add_edge('B', 'H', weight=34)
    G3.add_edge('B', 'F', weight=36)
    G3.add_edge('C', 'F', weight=42)
    G3.add_edge('C', 'E', weight=65)
    G3.add_edge('D', 'E', weight=33)
    G3.add_edge('F', 'H', weight=24)
    G3.add_edge('E', 'F', weight=18)
    G3.add_edge('D', 'I', weight=30)
    G3.add_edge('E', 'G', weight=23)
    G3.add_edge('F', 'G', weight=39)
    G3.add_edge('H', 'I', weight=19)
    G3.add_edge('G', 'I', weight=21)
    G3.add_edge('G', 'H', weight=25)
    # Apply this graph to Dijkstra's algorithm, starting with 'A'
    print("Dijkstra's algorithm with problem 4 graph:", list(nx.single_source_dijkstra(G3, 'A')))


def main():
    # Define the first graph from problem 1
    graph1 = {'a': set(['b', 'e', 'f']),
              'b': set(['a', 'c', 'f']),
              'c': set(['b', 'd', 'g']),
              'd': set(['c', 'g']),
              'e': set(['a', 'f', 'i']),
              'f': set(['a', 'b', 'e', 'i']),
              'g': set(['c', 'd', 'j']),
              'i': set(['e', 'f', 'j', 'm']),
              'j': set(['g', 'i']),
              'm': set(['i', 'n']),
              'n': set(['m']),
              'h': set(['l', 'k']),
              'k': set(['h', 'l', 'o']),
              'o': set(['k']),
              'l': set(['h', 'p']),
              'p': set(['l'])}

    # Do problem 1
    problem_1(graph1)

    # Problem 2
    v = dfs_paths(graph1, 'h', 'p')
    print("DFS path from h to p: ", list(v))
    w = bfs_path(graph1, 'h', 'p')
    print("BFS path from h to p: ", list(w))

    # Do problem 3
    problem_3()

    # Do problem 4
    problem_4()


if __name__ == "__main__":
    main()
