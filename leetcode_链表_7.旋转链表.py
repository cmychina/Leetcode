"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

"""
from linklist import *
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        ans=ListNode(-1)
        fast,slow=head,head
        #判断链表长度与k之间的关系
        cur=head
        n=0
        while cur:
            cur=cur.next
            n+=1
        if n==0 or k%n==0:
            return head
        n=k%n
        for i in range(n):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        tmp=slow.next
        fast.next=head
        ans.next=tmp
        slow.next=None
        return ans.next
if __name__=="__main__":
    a=[1,2,3,4,5]
    k=2
    l1=convert.list2link(a)
    s=Solution()
    out=s.rotateRight(l1,k)
    print(convert.link2list(out))
    a=[0,1,2]
    k=4
    l1=convert.list2link(a)
    s=Solution()
    out=s.rotateRight(l1,k)
    print(convert.link2list(out))
