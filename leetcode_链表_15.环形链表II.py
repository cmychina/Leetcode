"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

"""
from linklist import *
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast=head,head
        while slow!=fast:
            slow=slow.next
            fast=fast.next.next
        #第一次相遇的时候，快指针比慢指针多走了一个环的距离
        cur=head
        while cur!=slow:
            cur=cur.next
            slow=slow.next
        return slow