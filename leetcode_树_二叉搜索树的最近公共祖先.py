"""
二叉搜索树的 左子树值都小于右子树
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        # if p.val >q.val:
        #     p,q =q,p
        # while True:
        #     #说明p q都在左子树
        #     if root.val>q.val:
        #         root = root.left
        #     elif root.val < p.val:
        #         root = root.right
        #     else:
        #         return root