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
        visit = {}
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node] = Node(node.val)
            for neighbor in node.neighbors:
                visit[neighbor] = dfs(neighbor)
                visit[node].neighbors.append(visit[neighbor])
            return visit[node]
        return dfs(node)
            