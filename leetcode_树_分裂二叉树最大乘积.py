class Solution:
    def maxProduct(self,root):
        ans=[]
        def dfs(root):
            if not root:
                return 0
            sum=dfs(root.left)+dfs(root.right)+root.val
            ans.append(sum)
            return sum

        total=dfs(root)
        max_num=float("-inf")
        for sum in ans:
            max_num=max(max_num,(total-sum)*sum)
        return max_num