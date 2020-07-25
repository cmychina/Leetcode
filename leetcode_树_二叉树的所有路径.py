class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans=[]
        def dfs(root, tmp):
            if not root:
                return
            if not root.left and not root.right:
                tmp+=[str(root.val)]
                ans.append(tmp)
            dfs(root.left, tmp+[str(root.val)])
            dfs(root.right, tmp+[str(root.val)])
            return ans
        ans=dfs(root,[])
        return ["->".join(x) for x in ans]