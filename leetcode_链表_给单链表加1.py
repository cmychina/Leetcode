"""
先翻转链表，然后借助两数相加的原理加(考虑进位)，最后再翻转
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def reverseList(head):
            if not head or not head.next:
                return head
            cur = reverseList(head.next)
            tmp = head.next
            tmp.next = head
            head.next = None
            return cur

        head = reverseList(head)
        p = head
        carry = 1
        while p:
            carry, b = divmod(p.val + carry, 10)
            p.val = b
            if carry == 0:
                break
            if not p.next and carry:
                p.next = ListNode(0)
            p = p.next

        return reverseList(head)





