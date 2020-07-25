"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：

给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
"""
from linklist import  *
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        #标记当前头结点 去判断翻转节点,若长度不够，则不翻转
        #head=[1,2,3,4,5,6,7]
        #tail=[4,5,6,7]
        tail=head
        for i in range(k):
            if tail==None:
                return head
            tail=tail.next
        #[3,2,1]
        newhead=self.reverse(head,tail)
        head.next=self.reverseKGroup(tail,k)
        return newhead

    #翻转head到tail之间的部分
    def reverse(self,head,tail):
        pre=None
        while head!=tail:
            tmp=head.next
            head.next=pre
            pre=head
            head=tmp
        return pre

if __name__=="__main__":
    a=[1,2,3,4,5,6,7]
    k=3
    l1=convert.list2link(a)
    s=Solution()
    out=s.reverseKGroup(l1,k)
    print(convert.link2list(out))
