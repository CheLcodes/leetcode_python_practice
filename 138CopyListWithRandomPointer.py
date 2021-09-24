class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_dic = dict()
        cur = head
        while cur:
            node = Node(cur.val, None, None)
            node_dic[cur] = node
            cur = cur.next
        cur = head

        while cur:
            new_node = node_dic[cur]
            if cur.next:
                new_node.next = node_dic[cur.next]
            if cur.random:
                new_node.random = node_dic[cur.random]
            cur = cur.next

        return node_dic[head]
