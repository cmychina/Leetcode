class ListNode:
    pass

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