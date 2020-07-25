class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next: #开始走位
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 相遇
                break
        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow