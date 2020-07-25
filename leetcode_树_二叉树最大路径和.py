class Solution:

    def maxPathSum(self, root) -> int:
        self.ans=float("-inf")
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            #经过经前节点，加上左右
            self.ans=max(self.ans,left+right+root.val)
            #每个父节点返回，左右子树中最大的加上该父节点
            return max(0,max(left,right)+root.val)
        dfs(root)
        return self.ans