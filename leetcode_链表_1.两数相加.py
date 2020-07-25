"""

给出两个非空的链表用来表示两个非负的整数。
其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
from linklist import ListNode
class Solution:
    def addTwoNum(self,l1,l2):
        ans=ListNode(-1)
        cur=ans
        #表示进位
        flag=0
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            s=flag+x+y
            flag=s//10
            #余数
            cur.next=ListNode(s%10)
            cur=cur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if flag>0:
            cur.next=ListNode(1)
        return ans.next

class Solution2:
    def addTwoNum(self,l1,l2):
        ans=ListNode(0)
        if not l1:
            return l2
        if not l2:
            return l1
        val=l1.val+l2.val
        ans=ListNode(val%10)
        ans.next=self.addTwoNum(l1.next,l2.next)
        if val>=10:
            ans.next=self.addTwoNum(ListNode(1),ans.next)
        return ans



    def Mundane(self,l1,l2):

        if not l1:
            return l2
        if not l2:
            return l1
        val=l1.val+l2.val
        ans=ListNode(val%10)
        ans.next=self.addTwoNum(l1.next,l2.next)
        if val>=10:
            ans.next=self.addTwoNum(ListNode(1),ans.next)

        return ans


#两数相加II
class Solution:
    """
    输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 8 -> 0 -> 7
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=""
        s2=""
        p=l1
        q=l2
        while p:
            s1+=str(p.val)
            p=p.next
        while q:
            s2+=str(q.val)
            q=q.next
        res=str(int(s1)+int(s2))

        ans=ListNode(-1)
        pre=ans
        for i in res:
            pre.next=ListNode(i)
            pre=pre.next
        return ans.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        node = None
        carry = 0

        while stack1 or stack2:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0

            val= x + y + carry
            carry = val // 10
            n = val % 10
            cur = ListNode(n)
            cur.next = node#!!!!!!!!!!!!!!!!!!尾插法
            node = cur
        # 判断最高位是否有进位
        if carry != 0:
            res = ListNode(carry)
            res.next = cur
            return res
        return cur


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
    a=[4,4,4]
    b=[4,6,4]
    l1=list2link(a)
    l2=list2link(b)
    s=Solution()
    out=s.addTwoNum(l1,l2)
    print(link2list(out))

