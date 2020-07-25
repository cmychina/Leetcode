"""
对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）

"""
class TreeNode:
    pass
#二叉搜索树的最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val:
            p, q = q, p
        while True:
            #说明p q都在左子树
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                return root
#2.二叉树的最近公共祖先
def lowestCommonAncestor(self, root, p, q):
    self.result = TreeNode(float("inf"))
    def dfs(root):
        if not root:
            return False
        left_result = dfs(root.left)
        right_result = dfs(root.right)
        #当前节点为目标节点
        if root.val == p.val or root.val == q.val:
            #左右分支有一个包含目标值
            if left_result or right_result:
                self.result = root
            return True
        #目标值在当前节点的左右分支
        if left_result and right_result:
            self.result = root
            return True
        if left_result or right_result:
            return True
    dfs(root)
    return self.result