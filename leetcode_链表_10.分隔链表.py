"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

思路：双链表分别记录大于x和小于x的
"""
from linklist import *
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        d1=ListNode(-1)
        d2=ListNode(-1)
        p1=d1
        p2=d2
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
                head=head.next
            else:
                p2.next=head
                p2=p2.next
                head=head.next
        p1.next=d2.next
        p2.next=None
        return d1.next

if __name__=="__main__":
    a=[1,4,3,2,5,2]
    x=3
    l1=convert.list2link(a)
    s=Solution()
    out=s.partition(l1,x)
    print(convert.link2list(out))

