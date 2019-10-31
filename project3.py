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
    print("DFS path from a to c: ", list(v))
    w = bfs_path(graph1, 'h', 'p')
    print("BFS path from a to c: ", list(w))
    # Problem 3
    G2 = nx.Graph()
    G2.add_edges_from([(1, 3), (3, 5), (3, 2), (2, 1), (4, 1),
                       (4, 2), (4, 12), (11, 12), (3, 5),
                       (5, 6), (5, 8), (6, 8), (6, 7), (6, 10),
                       (10, 9), (8, 9), (8, 10), (7, 10), (10, 11)])


if __name__ == "__main__":
    main()
