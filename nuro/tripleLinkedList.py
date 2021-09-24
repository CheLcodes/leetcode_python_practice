class Node:
    def __init__(self, val, next=None, triple_next=None):
        self.val = val
        self.next = next
        self.triple_next = triple_next


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.list_size = 0
    
    def get_prev_nodes(self, k): # find prev 3 nodes for kth node
        p3, p2, p1 = Node(float('inf')), Node(float('inf')), Node(float('inf'))
        p3.next = p2
        p2.next = p1
        p1.next = self.head

        while k and p1:
            p3 = p2
            p2 = p1
            p1 = p1.next
            k -= 1
        
        if p1.val == float('inf'):
            p1 = None
        if p2.val == float('inf'):
            p2 = None
        if p3.val == float('inf'):
            p3 = None
        return p3, p2, p1


    def insert_node_at_kth(self, k, val):
        if k < 0 or k > self.list_size:
            raise Exception('Invalid position')
        self.list_size += 1
        new_node = Node(val)
        # k-3, k-2, k-1, k, k+1, k+2, k+3
        prev_3, prev_2, prev_1 = self.get_prev_nodes(k)
        # insert at head
        if not prev_1 and not prev_2 and not prev_3:
            if self.list_size > 1:
                new_node.next = self.head
            if self.head.next and self.head.next.next:
                new_node.triple_next = self.head.next.next
            self.head = new_node
            return self.head
        else:
            after_1 = prev_1.next
            after_2 = after_1.next if after_1 else None
            after_3 = prev_1.triple_next
        prev_1.next = new_node
        new_node.next = after_1
        new_node.triple_next = after_3
        prev_1.triple_next = after_2
        if prev_2:
            prev_2.triple_next = after_1
        if prev_3:
            prev_3.triple_next = new_node
        return self.head   
    

    def remove_node(self, k):
        if k < 0 or k > self.list_size:
            raise Exception('Invalid position')
        self.list_size -= 1
        prev_3, prev_2, prev_1 = self.get_prev_nodes(k)
        # remove head
        if not prev_1 and not prev_2 and not prev_3:
            if self.head and self.head.next:
                self.head = self.head.next
            else:
                self.head = Node(None)
            return self.head
        else:
            after_1 = prev_1.next.next if prev_1.next else None
            after_2 = after_1.next if after_1 else None
            after_3 = after_2.next if after_2 else None
        # k-3, k-2, k-1, k, k+1, k+2, k+3
        prev_1.next = after_1
        prev_1.triple_next = after_3
        prev_2.triple_next = after_2
        prev_3.triple_next = after_1
        return self.head
    

    def print_list(self):
        curr = self.head
        while curr:
            print('node value', curr.val)
            if curr.triple_next:
                print('triple next', curr.triple_next.val)
            else:
                print('triple next is empty')
            curr = curr.next


def testLinkedList():
    my_list = LinkedList()
    my_list.insert_node_at_kth(0, 1)
    my_list.insert_node_at_kth(1, 2)
    my_list.insert_node_at_kth(2, 3)
    my_list.insert_node_at_kth(3, 4)
    my_list.insert_node_at_kth(2, 5)
    my_list.remove_node(3)
    my_list.remove_node(0)
    # my_list.remove_node(8)
    my_list.print_list()


testLinkedList()