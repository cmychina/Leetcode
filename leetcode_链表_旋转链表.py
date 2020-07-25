"""
slow和fast之间的距离就是k的距离

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        ans = ListNode(-1)
        ans.next = head
        cur = head
        n = 0
        slow, fast = head, head
        while cur:
            cur = cur.next
            n += 1
        if n == 0 or k % n == 0:
            return head
        k = k % n
        while fast.next and k > 0:
            fast = fast.next
            k -= 1
        # 反之fast走到结尾
        while fast.next:
            slow = slow.next
            fast = fast.next
        # fast到最后一个，slow到需要断开的地方
        fast.next = head
        ans.next = slow.next
        slow.next = None
        return ans.next

#构成一个环
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        pre = head
        n = 0
        while head:
            n += 1
            if not head.next:
                break
            head = head.next
        head.next = pre

        head.next = pre
        k = k % n
        move = n - k

        while move:
            pre = pre.next
            head = head.next
            move -= 1
        head.next = None
        return pre

