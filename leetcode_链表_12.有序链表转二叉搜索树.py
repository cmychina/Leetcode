"""

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

思路:快慢指针找到中点，递归的处理左右子树。

"""
from linklist import *
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findmid(head, tail):
            slow = head
            fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow

        def helper(head, tail):
            if head == tail:
                return
            node = findmid(head, tail)
            root = TreeNode(node.val)
            root.left = helper(head, node)
            root.right = helper(node.next, tail)
            return root

        return helper(head, None)

if __name__=="__main__":
    a=[-10, -3, 0, 5, 9]
    l1=convert.list2link(a)
    s=Solution()
    out=s.sortedListToBST(l1)
    print(convert.tree2list(out))