"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
输入: 1->1->2
输出: 1->2

输入: 1->1->2->3->3
输出: 1->2->3
"""
from linklist import *
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans=ListNode(-1)
        ans.next=head
        while head and head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return ans.next

#借用集合
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # 用集合
        val_set = set()
        pre = ListNode(-1)
        pre.next = head
        while pre.next:
            if pre.next.val in val_set:
                pre.next = pre.next.next
            else:
                val_set.add(pre.next.val)
                pre = pre.next

        return head
if __name__=="__main__":
    a=[1,1,2,3,3]
    l1=convert.list2link(a)
    s=Solution()
    out=s.deleteDuplicates(l1)
    print(convert.link2list(out))
