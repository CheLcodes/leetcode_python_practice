class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def compactTree(self, root: Node, N):
        new_root = Node(root.val)
        queue, new_queue = [], []
        self.bfs(root, queue)
        new_queue.append(new_root)

        while queue:
            new_node = new_queue.pop(0)
            i = 0
            while i < N and queue:
                    nxt = queue.pop(0)
                    self.bfs(nxt, queue)
                    new_nxt = Node(nxt.val)
                    new_node.children.append(new_nxt)
                    new_queue.append(new_nxt)
                    i += 1
        return new_root

    def bfs(self, node, queue):
        for c in node.children:
            queue.append(c)
        # return node
                
# Tree
n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')
n7 = Node('G')
n8 = Node('H')

nodes = [n1, n2, n3, n4, n5, n6, n7, n8]

n1.children = [n2]
n2.children = [n3, n5]
n3.children = [n4]
n4.children = [n6]
n5.children = [n7, n8]

sol = Solution()
res = sol.compactTree(n1, 1)


def traverse(node):
    queue = [node]
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            print(node.val)
            for c in node.children:
                queue.append(c)
        print('==================')

traverse(res)    
# print('nodes:', nodes)





