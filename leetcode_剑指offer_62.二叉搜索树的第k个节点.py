"""
可以用迭代直接在k处停止
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #中序遍历递增
        if k==0 :
            return None
        self.res=[]
        def dfs(pRoot):
            if not pRoot:
                return None
            dfs(pRoot.left)
            self.res.append(pRoot)
            if len(self.res)==k:
                return self.res[k-1]
            dfs(pRoot.right)
        dfs(pRoot)
        return  None
