

class Solution:

    def levelOrder(root):
        res = []
        if not root:
            return res
        level = [root]
        while level:
            res.append([node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return res

    def levelOrder(root):
        res = []
        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res