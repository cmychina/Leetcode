"""
给定一个链表，判断链表中是否有环。为了表示给定链表中的环，
我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
输入：head = [3,2,0,-4], pos = 1
输出：true
"""
from linklist import *
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
