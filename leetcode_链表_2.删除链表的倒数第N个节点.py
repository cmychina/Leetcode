"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
进阶：
你能尝试使用一趟扫描实现吗？
思路：快慢指针
"""
from linklist import ListNode
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head or not head.next:
            return head
        fast,slow=head,head
        for i in range(n):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        #slow此时定位的下一个节点就是要删除的节点
        slow.next=slow.next.next
        return head

def list2link(li):
    n=len(li)
    ans=ListNode(-1)
    cur=ans
    for i in range(n):
        cur.next=ListNode(li[i])
        cur=cur.next
    return ans.next

def link2list(li):
    ans=[]
    while li:
        ans.append(li.val)
        li=li.next
    return ans

if __name__=="__main__":
    a=[1,2,3,4,5]
    n=2
    head=list2link(a)
    s=Solution()
    out=s.removeNthFromEnd(head,n)
    print(link2list(out))

