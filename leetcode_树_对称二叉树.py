class Solution:
    def isSymmetrical(self, root):
        if not root:
            return True
        def dfs(left, right):
            if left == right:
                return True
            if not (left and right):
                return False
            if left.val!=right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)