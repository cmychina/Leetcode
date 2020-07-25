"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
from linklist import *
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        slow,fast=head,head
        for i in range(m):
            slow=slow.next