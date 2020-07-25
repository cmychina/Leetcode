"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""
from linklist import ListNode,convert
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur=head.next
        head.next=self.swapPairs(cur.next)
        cur.next=head
        return cur

    def Mundane(self,head):

        ans = ListNode(-1)
        ans.next = head
        pre = ans
        cur = ans.next
        while cur and cur.next:
            tmp = cur.next
            pre.next = tmp
            cur.next = tmp.next
            tmp.next = cur
            pre = cur
            cur = cur.next
        return ans.next




if __name__=="__main__":
    a=[1,2,3,4,5,6]
    l1=convert.list2link(a)
    s=Solution()
    out=s.swapPairs(l1)
    print(convert.link2list(out))