"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
"""
#len(self.res) == depth关键点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) :

        def dfs(node, depth):
            if not node:
                return
            if len(self.res) == depth:
                self.res.append(node.val)
            dfs(node.right,depth + 1)
            dfs(node.left,depth + 1)
        self.res=[]
        dfs(root, 0)
        return self.res
    
import  collections
#BFS
class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        res = []
        def bfs(root):
            queue = [root]
            while queue:
                nxt = []
                res.append(queue[-1].val)
                for node in queue:
                    if node.left:
                        nxt.append(node.left)
                    if node.right:
                        nxt.append(node.right)
                queue = nxt
        bfs(root)
        return res
