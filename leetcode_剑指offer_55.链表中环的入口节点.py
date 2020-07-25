class Solution:
    def EntryNodeOfLoop(self, head):
        # write code here
        if not head:
            return None
        slow,fast=head,head
        flag=False
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                flag=True
                break
        if flag:
            ans=head
            while slow!=ans:
                slow=slow.next
                ans=ans.next
            return ans
        else:
            return None