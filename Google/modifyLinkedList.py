"""
https://www.1point3acres.com/bbs/thread-778605-1-1.html
寫出把第N個Node的值更新為M的方程。
值得注意的是如果第N個Node的值更新了，第 N - 1 個 Node 的 hashVal 也要更新， N - 2 也要更新， 以此類推。
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.hashVal = None
        self.next = None

def setHash(node: Node): 
    if node.next:
        node.hashVal = hash(node.next.val + node.val)
    else:
        node.hashVal = hash(node.val) 
    


class Solution:
    def modifyNode(self, head: Node, N, M):
        curr = head
        stack = []
        i = 0
        while i < N:
            stack.append(curr)
            curr = curr.next
            i += 1

        curr.val = M
        setHash(curr)

        while stack:
            node = stack.pop()
            setHash(node)
        return head

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

nodes = [n1, n2, n3, n4, n5]
for n in nodes:
    setHash(n)

res = Solution().modifyNode(n1, 3, 6)
curr = res
while curr:
    print('hashval==', curr.hashVal)
    curr = curr.next
             

