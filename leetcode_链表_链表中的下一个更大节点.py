"""
单调栈的问题
可以转成数组
也可以直接操作链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode):
        stack = []
        stack_loc = []
        loc = -1
        res = []
        while head:
            loc += 1
            res.append(0)
            while stack and stack[-1] < head.val:
                res[stack_loc[-1]] = head.val
                stack.pop()
                stack_loc.pop()
            stack.append(head.val)
            stack_loc.append(loc)
            head = head.next

        return res

#转数组做
class Solution:
    def nextLargerNodes(self, head: ListNode):
        nums = []
        stack = []
        total=0
        while head:
            nums.append(head.val)
            head= head.next
            total+=1
        ans = [0]* total
        for i in range(total):
            while stack and nums[stack[-1]]<nums[i]:
                ans[stack.pop()] = nums[i]
            #stack记录单调索引
            stack.append(i)
        return ans

