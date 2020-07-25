class Solution:
    def closestValue(self, root, target):
        self.res=float("inf")
        self.ans=0
        def dfs(root):
            if not root:
                return
            if abs(root.val-target)<=self.res:
                self.res=abs(root.val-target)
                self.ans=root.val
            if root.val<target:
                dfs(root.right)
            else:
                dfs(root.left)
        dfs(root)
        return self.ans