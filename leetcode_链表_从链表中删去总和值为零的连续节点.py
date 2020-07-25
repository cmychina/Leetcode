class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    关键点：
    如果i-j之间的和为0
    那么0-i和0-j之间的和是相等的
    [1,2,3,-3,4]
    [0,1,2,3,4] 0-1的和为3，0-3的和为3，所以2-3的和是0.
    """
    def removeZeroSumSublists(self, head):
        l = ListNode(0)
        l.next = head
        d = {0:l}
        s = 0
        while head:
            s+=head.val
            if s in d:
                d[s].next = head.next
                return self.removeZeroSumSublists(l.next)
            else:
                d[s] = head
                head = head.next
        return l.next
    
    def Mundane(self,head):
        l = ListNode(0)
        l.next = head
        d={0:l}
        node, s = head, 0
        while node:
            s += node.val
            if s not in d:
                d[s] = node
            else:
                node = d[s].next
                tmp = node.val + s
                # 同前缀和的两点之间的节点删掉
                while tmp != s:
                    del d[tmp]
                    node = node.next
                    tmp += node.val
                # 删掉两点之间的后，接上不重复的段
                d[s].next = node.next
            node = node.next
        return l.next