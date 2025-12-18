from collections import deque
from typing import Dict, List

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Breadth-First Search (BFS)

    Traverses a graph level by level starting from the given node.
    Time Complexity: O(V + E)
    """
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph.get(node, []))

    return order


if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: []
    }
    print(bfs(graph, 1))
