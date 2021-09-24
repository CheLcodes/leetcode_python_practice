class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.parent = None
        self.child = None

class Solution:
    def flattenList(self, head: 'Node', tail: 'Node'):
        move = head

        while move:
            if move.child:
                tail.next = move.child
                move.child.prev = tail
                tail = tail.next
                while tail.next:
                    tail = tail.next
                move.child = None
            if move.parent:
                tail.next = move.parent
                move.parent.prev = tail
                tail = tail.next
                while tail.next:
                    tail = tail.next
                move.parent = None
            move = move.next
        return head


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

n1.next = n2
n2.next = n3
n3.next = n4

n2.parent = n5
n5.next = n6
n6.next = n7
n6.parent = n8

n2.child = n9

sol = Solution()
res = sol.flattenList(n1, n4)

while res:
    print(res.val)
    res = res.next

