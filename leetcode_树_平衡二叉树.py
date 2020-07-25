"""
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""
class solution:
    def isBalanced(self,root):
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if abs(right - left) > 1:
                self.res = False
            return max(left, right) + 1
        helper(root)
        return self.res