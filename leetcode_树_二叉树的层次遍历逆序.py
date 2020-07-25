"""
给定一个二叉树，返回其节点值自底向上的层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""
class Solution:
    def levelOrderBottom(root):
        res = []
        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.insert(0, [])
            res[-(depth + 1)].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res

    def levelOrderBottom(root):
        from collections import deque
        if not root:
            return []
        queue = deque()
        queue.appendleft(root)
        res = []
        while queue:
            tmp = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop()
                tmp.append(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            res.insert(0, tmp)
        return res