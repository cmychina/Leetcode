"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
思路：快慢指针找到中点Lm，然后将Lm后面的翻转得 Ln,Ln-1,Ln-2
然后得到两个序列L0,L1,...Lm和Ln,Ln-1,Ln-2，然后交替连接即可
#交替连接，首先保存左右的next，然后将左指针连接到右指针，把右指针和左next连接
然后更新左右指针
"""

from linklist import *
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head==None or head.next==None:
            return head
        #快慢指针找中点
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        right_reverse=slow.next
        slow.next=None
        right_reverse=self.reverse(right_reverse)##4->3

        #指针
        left_cur=head
        right_cur=right_reverse
        while left_cur and right_cur:
            #保存右侧指针
            right_next=right_cur.next
            left_next=left_cur.next
            #连接
            right_cur.next=left_cur.next
            left_cur.next=right_cur
            #更新指针
            left_cur=left_next
            right_cur=right_next
        return head

    def reverse(self, head: ListNode):
        if head == None or head.next == None:
            return head
        tmp = head.next
        cur = self.reverse(tmp)
        tmp.next = head
        head.next = None
        return cur

if __name__=="__main__":
    a=[1,2,3,4,5,6]
    l1=convert.list2link(a)
    s=Solution()
    out=s.reorderList(l1)
    print(convert.link2list(out))