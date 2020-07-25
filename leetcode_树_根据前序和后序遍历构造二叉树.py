"""
前序遍历为 (根结点) (前序遍历左分支) (前序遍历右分支)

后序遍历为 (后序遍历左分支) (后序遍历右分支) (根结点)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre:
            return None
        node = TreeNode(pre[0])
        if len(pre) == 1:
            return node
        i = post.index(pre[1])+1

        node.left = self.constructFromPrePost(pre[1:i + 1], post[:i ])
        node.right = self.constructFromPrePost(pre[i + 1:], post[i:-1])

        return node