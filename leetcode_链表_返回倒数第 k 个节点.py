"""
快慢指针，快指针先走k 快慢一起走
"""

class Solution:
    def kthToLast(self, head, k: int) -> int:
        slow,fast=head,head
        for _ in range(k):
            fast=fast.next
        if not fast:
            return head.val
        while fast.next:
            slow=slow.next
            fast=fast.next
        return slow.next.val