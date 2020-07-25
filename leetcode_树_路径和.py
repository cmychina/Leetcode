class Solution:
    def hasPathSum(self,root,target):
        if not root:
            return False
        self.res=False
        def dfs(root,target):
            if not root:
                return
            if root.val==target and not root.left and not root.right:
                self.res=True
            dfs(root.left,target-root.val)
            dfs(root.right,target-root.val)
        dfs(root,target)
        return self.res

    def pathSumII(self,root,target):
        if not root:
            return False
        res=[]

        def dfs(root, target,tmp):
            if not root:
                return
            if root.val == target and not root.left and not root.right:
                tmp.append(root.val)
                res.append(tmp)
            dfs(root.left, target - root.val,tmp+[root.val])
            dfs(root.right, target - root.val,tmp+[root.val])

        dfs(root, target,[])
        return res

    def pathSumIII(self,root,target):
        if not root:
            return
        self.cnt=0
        def dfs(root,target):
            if not root:
                return
            if root.val == target:
                self.cnt+=1
            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)

        queue=[root]
        while queue:
            next=[]
            for node in queue:
                dfs(node,target)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            queue=next
        return self.cnt

