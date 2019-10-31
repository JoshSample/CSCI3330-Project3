"""
Josh Sample, Jack Thurber, Anthony Sweeney
CSCI 3330
11/3/2019
"""
import networkx as nx  # This is the graph ADT we are working with


def main():
    # Instantiate G1 as a graph object
    G1 = nx.Graph()
    # Define the first graph from problem 1
    graph1 = {"a": ["b", "f", "e"],
              "b": ["a", "c", "f"],
              "c": ["b", "d", "g"],
              "d": ["c", "g"],
              "e": ["a", "f", "i"],
              "f": ["a", "b", "e", "i"],
              "g": ["c", "d", "j"],
              "i": ["e", "f", "j", "m"],
              "j": ["g", "i"],
              "m": ["i", "n"],
              "n": ["m"],
              "h": ["l", "k"],
              "k": ["h", "l", "o"],
              "o": ["k"],
              "l": ["h", "p"],
              "p": ["l"]}
    for k, v in graph1.items():
        for vv in v:
            G1.add_edge(k, vv)

    # Problem 1
    print("DFS:", list(nx.dfs_edges(G1, "a")))
    print("DFS with other remaining edges:", list(nx.dfs_edges(G1, "h")))
    print("BFS:", list(nx.bfs_edges(G1, "a")))
    print("BFS with other remaining edges:", list(nx.bfs_edges(G1, "h")))
    # Problem 2

    # Problem 3
    G2 = nx.Graph()
    G2.add_edges_from([(1, 3), (3, 5), (3, 2), (2, 1), (4, 1),
                       (4, 2), (4, 12), (11, 12), (3, 5),
                       (5, 6), (5, 8), (6, 8), (6, 7), (6, 10),
                       (10, 9), (8, 9), (8, 10), (7, 10), (10, 11)])


if __name__ == "__main__":
    main()
