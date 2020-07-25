"""
left-right-root
"""
class Solution:
    #迭代
    def postorderTraversal(root):
        res = []
        cur = root
        stack = []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            tmp = stack.pop()
            cur = tmp.left
        return res[::-1]
    
    #递归
    def postorderTraversal(root):
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)

        helper(root)
        return res




