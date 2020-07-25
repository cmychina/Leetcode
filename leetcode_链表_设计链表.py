"""
dummy头结点
"""
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=Node(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0:
            return -1
        node=self.node
        for _ in range(index+1):
            if node.next is not None:
                node=node.next
            else:
                return -1
        return  node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newHead=Node(val)
        newHead.next=self.head.next
        self.head.next=newHead

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node=self.head
        while node.next:
            node=node.next
        node.next=Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self.head
        for i in range(index):
            if node is None:
                return
            node = node.next
        if node is None:
            node = Node(val)
        else:
            new = Node(val)
            new.next = node.next
            node.next = new

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0: return
        node = self.head
        for _ in range(index):
            node = node.next
        if node.next is not None:
            node.next = node.next.next

#双链表实现
class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev, self.next = None, None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummyhead = ListNode(0)
        self.dummytail = ListNode(0)
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        if index < self.size - 1 - index:
            node = self.dummyhead
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            node = self.dummytail
            for _ in range(self.size - index):
                node = node.prev
            return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index < self.size - index:
            prev = self.dummyhead
            for _ in range(index):
                # print(node.val,self.size)
                prev = prev.next
            newnode = ListNode(val)
            next = prev.next
            prev.next = newnode
            newnode.prev = prev
            newnode.next = next
            next.prev = newnode

            self.size += 1
        else:
            next = self.dummytail
            for _ in range(self.size - index):
                next = next.prev
            newnode = ListNode(val)
            prev = next.prev
            prev.next = newnode
            newnode.prev = prev
            newnode.next = next
            next.prev = newnode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.size - 1:
            return
        if index < self.size - 1 - index:
            node = self.dummyhead
            for _ in range(index):
                node = node.next
            node.next = node.next.next
            node.next.prev = node
            self.size -= 1
        else:
            node = self.dummytail
            for _ in range(self.size - 1 - index):
                node = node.prev
            node.prev = node.prev.prev
            node.prev.next = node
            self.size -= 1



