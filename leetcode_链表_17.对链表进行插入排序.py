"""
每次比较，遇到比当前值小的，就将其插入到头结点(这里面是dummy后的第一个节点)
"""
from linklist import *
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ans=ListNode(-1)
        ans.next=head
        while head and head.next:
            if head.val<=head.next.val:
                head=head.next
            else:
                #pre用来排序
                pre=ans
                while pre.next.val<head.next.val:
                    pre=pre.next
                #找到第一个比当前值小的
                cur=head.next
                head.next=cur.next
                cur.next=pre.next
                pre.next=cur
                print(convert.link2list(pre))
                print(head.val)
        return ans.next
if __name__=="__main__":
    a=[4,2,1,3]
    l1=convert.list2link(a)
    s=Solution()
    out=s.insertionSortList(l1)
    print(convert.link2list(out))