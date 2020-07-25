"""
同two_sum
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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
