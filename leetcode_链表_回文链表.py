"""
编写一个函数，检查输入的链表是否是回文的。
思路：快慢指针找中点，然后将后面的链表翻转，然后比较翻转后的链表和头结点的值。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if head == None or head.next == None:
            return True

        p = ListNode(-1)
        p.next = head
        slow, fast = p, p
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #找到中点，将后面翻转
        tmp = self.reverse(slow.next)
        while tmp:
            if head.val != tmp.val:
                return False
            head = head.next
            tmp = tmp.next
        return True

    def reverse(self, node: ListNode) -> ListNode:
        if node == None or node.next == None:
            return node
        tmp = node.next
        ans = self.reverse(tmp)
        tmp.next = node
        node.next = None
        return ans