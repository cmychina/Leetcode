"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
输入: 1->2->3->3->4->4->5
输出: 1->2->5

输入: 1->1->1->2->3
输出: 2->3
"""
from linklist import *
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans=ListNode(-1)
        ans.next=head
        pre=ans
        while pre.next and pre.next.next:
            if pre.next.val==pre.next.next.val:
                tmp=pre.next.val
                cur=pre.next
                while cur and cur.val==tmp:
                    cur=cur.next
                pre.next=cur
            else:
                pre=pre.next
        return ans.next
if __name__=="__main__":
    a=[1,2,3,3,4,4,5,5]
    l1=convert.list2link(a)
    s=Solution()
    out=s.deleteDuplicates(l1)
    print(convert.link2list(out))