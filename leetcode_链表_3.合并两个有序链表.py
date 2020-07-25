from linklist import  ListNode
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=ListNode(-1)
        cur=ans
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        if l1:
            cur.next=l1
        if l2:
            cur.next=l2
        return ans.next

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
    a=[1,2,4]
    b=[1,3,4]
    l1=list2link(a)
    l2=list2link(b)
    s=Solution()
    out=s.mergeTwoLists(l1,l2)
    print(link2list(out))