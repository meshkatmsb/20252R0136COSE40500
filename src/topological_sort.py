from collections import deque
from typing import Dict, List

def topological_sort(graph: Dict[str, List[str]]) -> List[str]:
    """
    Topological Sort using Kahn's Algorithm.

    Works only for Directed Acyclic Graphs (DAGs).

    Time Complexity: O(V + E)
    """
    in_degree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph):
        raise ValueError("Graph contains a cycle")

    return order


if __name__ == "__main__":
    graph = {
        "A": ["C"],
        "B": ["C", "D"],
        "C": ["E"],
        "D": ["F"],
        "E": [],
        "F": []
    }

    print(topological_sort(graph))
