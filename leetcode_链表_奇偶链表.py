class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        p=head
        tmpHead=q=p.next
        while q and q.next:
            p.next=p.next.next
            q.next=q.next.next
            p,q=p.next,q.next
        p.next=tmpHead
        return head