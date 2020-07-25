class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup = {}
        def dfs(head):
            if not head:
                return None
            if head in lookup:
                return lookup[head]
            clone = Node(head.val, None, None)
            lookup[head] = clone
            clone.next, clone.random = dfs(head.next), dfs(head.random)
            return clone
        return dfs(head)


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        #复制节点
        cur=head
        while cur:
            tmp=cur.next
            cur.next=Node(cur.val,None,None)
            cur.next.next=tmp
            cur=tmp
        #复制随机节点
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        #拆分
        cur=head
        copy_head=head.next
        copy_cur=copy_head
        while copy_cur.next:
            cur.next=cur.next.next
            cur=cur.next
            copy_cur.next=copy_cur.next.next
            copy_cur=copy_cur.next






class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # 复制节点
        cur = head
        while cur:
            # 保存下一个节点
            tmp = cur.next
            # 后面跟着同样的节点
            cur.next = Node(cur.val, None, None)
            # 拼接
            cur.next.next = tmp
            cur = tmp
        # 复制random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分
        cur = head
        copy_head = head.next
        copy_cur = copy_head
        while copy_cur.next:
            # 组head
            cur.next = cur.next.next
            cur = cur.next
            # 组 copy_head
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next
        # 把链表结束置空
        cur.next = copy_cur.next
        copy_cur.next = None
        return copy_head
