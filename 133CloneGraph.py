"""
 Definition for a Node.
"""
import collections


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        node_copy = Node(node.val, [])
        node_dic = dict()
        queue = collections.deque()
        node_dic[node] = node_copy
        queue.append(node)

        while queue:
            origin_node = queue.popleft()
            if not origin_node: continue
            for n in origin_node.neighbors:
                if n not in node_dic:
                    node_dic[n] = Node(n.val, [])
                    queue.append(n)
                node_dic[n].neighbors.append(node_dic[n])
        return node_copy

# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_copy = self.dfs(node, dict())
        return node_copy

    def dfs(self, node, node_dic):
        if not node:
            return None
        if node in node_dic:
            return node_dic[node]
        node_copy = Node(node.val, [])
        node_dic[node] = node_copy
        for n in node.neighbors:
            n_copy = self.dfs(n, node_dic)
            if n_copy:
                node_dic[node_copy].neighbors.append(n_copy)
        return node_copy










