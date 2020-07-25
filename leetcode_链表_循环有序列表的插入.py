class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal,head)
            newNode.next = newNode
            return newNode

        p = head
        while p.next:
            if p.val <= insertVal <= p.next.val:
                break
            # 就一个值
            if p.next == head:
                break
            if p.val > p.next.val and (p.val <= insertVal or insertVal <= p.next.val):
                break
            p = p.next

        node = Node(insertVal)
        next = p.next
        p.next = node
        node.next = next

        return head