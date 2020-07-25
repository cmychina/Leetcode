class Solution:
    def closestValue(self, root, target, k):
        self.res=float("inf")
        self.ans=[]
        def dfs(root):
            if not root:
                return
            if abs(root.val-target)<=self.res:
                self.res=abs(root.val-target)
                self.ans.insert(0,root.val)
            if root.val<target:
                dfs(root.right)
            else:
                dfs(root.left)
        dfs(root)
        return self.ans[:k]