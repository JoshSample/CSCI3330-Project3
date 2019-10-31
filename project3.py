"""
Josh Sample, Jack Thurber, Anthony Sweeney
CSCI 3330
11/3/2019
"""
import networkx as nx  # This is the graph ADT we are working with


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def problem_1(graph):
    # Instantiate G1 as a graph object
    G1 = nx.Graph()
    # Add graph edges to G1 object
    for k, v in graph.items():
        for vv in v:
            G1.add_edge(k, vv)

    # Problem 1
    print("DFS:", list(nx.dfs_edges(G1, "a")))
    print("DFS with other remaining edges:", list(nx.dfs_edges(G1, "h")))
    print("BFS:", list(nx.bfs_edges(G1, "a")))
    print("BFS with other remaining edges:", list(nx.bfs_edges(G1, "h")))


def main():
    # Define the first graph from problem 1
    graph1 = {'a': set(['b', 'f', 'e']),
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
    v = dfs_paths(graph1, 'a', 'c')
    print("DFS path: ", list(v))
    # Problem 3
    G2 = nx.Graph()
    G2.add_edges_from([(1, 3), (3, 5), (3, 2), (2, 1), (4, 1),
                       (4, 2), (4, 12), (11, 12), (3, 5),
                       (5, 6), (5, 8), (6, 8), (6, 7), (6, 10),
                       (10, 9), (8, 9), (8, 10), (7, 10), (10, 11)])


if __name__ == "__main__":
    main()
