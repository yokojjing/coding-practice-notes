"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit = {node:Node(node.val)}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visit:
                    visit[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visit[cur].neighbors.append(visit[neighbor])
        return visit[node]
            