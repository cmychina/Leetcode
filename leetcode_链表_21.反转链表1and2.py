"""
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
from linklist import *
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        cur=head
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        return pre

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tmp=head.next
        cur=self.reverseList(tmp)
        tmp.next=head
        head.next=None
        return cur

#翻转链表2
class Solution:
    """
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转
    """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        tmpHead = ListNode(0)
        tmpHead.next = head
        node = tmpHead
        for i in range(1, m):
            node = node.next
        # node.next就是反转前的起点
        cur = node.next
        pre = None
        for i in range(m, n + 1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        print(cur)
        #这里的顺序不能搞错！！！！！！！
        node.next.next = tmp
        node.next = pre
        return tmpHead.next


if __name__=="__main__":
    a=[1,2,3,4,5]
    l1=convert.list2link(a)
    s=Solution()
    out=s.reverseList(l1)
    print(convert.link2list(out))