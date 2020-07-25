# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def __init__(self,res=[]):
    #     self.res=[]
    #
    # def inorderTraversal(self, root):
    #     if not root:
    #         return
    #     self.inorderTraversal(root.left)
    #     self.res.append(root.val)
    #     self.inorderTraversal(root.right)
    #
    #     return self.res

    def inorderTraversal(root):
        stack = []
        cur = root
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def inorderTraversal(root):
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res

# if __name__=='main':
#     s=Solution()
#     nums=[1,None,2,3]
#     print(s.inorderTraversal(nums))
