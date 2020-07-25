
class Solution:

    def zigzagLevelOrder(root):
        res = []
        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            #偶数从左到右，奇数从右到左
            if depth % 2 == 0:
                res[depth].append(root.val)
            else:
                res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res