"""
链表的快排与归并排序
"""
from linklist import *
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        归并排序，要找中点，链表中点用快慢指针
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        right=self.sortList(slow.next)
        slow.next=None#切断
        left=self.sortList(head)

        return self.mergesort(left,right)


    def mergesort(self,head1,head2):
        ans=ListNode(-1)
        pre=ans
        while head1 and head2:
            if head1.val<=head2.val:
                pre.next=head1
                head1=head1.next
                pre=pre.next
            else:
                pre.next=head2
                head2=head2.next
                pre=pre.next
        if head1:
            pre.next=head1
        if head2:
            pre.next=head2
        return ans.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        快排
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        ans = ListNode(-1)
        ans.next = head
        return self.quicksort(ans, None)

    def quicksort(self, head, end):
        if head == end or head.next == end or head.next.next == end:
            return head
        tmp = ListNode(-1)
        partition = head.next
        p = partition
        #用来记录排序结果？
        t = tmp
        while p.next!=end:
            if p.next.val < partition.val:
                t.next = p.next
                t = t.next
                p.next = p.next.next
            #大于partitio的val，不操作
            else:
                p = p.next
        t.next = head.next#head.next 是未排序前
        head.next = tmp.next

        self.quicksort(head, partition)
        self.quicksort(partition, end)
        return head.next



if __name__=="__main__":
    a=[4,5,3,6,1,7,8,2]
    l1=convert.list2link(a)
    s=Solution()
    out=s.sortList(l1)
    print(convert.link2list(out))
