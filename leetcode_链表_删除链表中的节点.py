class Solution:
    def deleteNode(self,node):
        """
        原地删除 秀
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next