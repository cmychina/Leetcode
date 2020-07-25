class Solution:
    def printTree(self, root):
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return 1 + max(left, right)


        m = depth(root)
        n = 2 ** m - 1
        res = [[""] * n for _ in range(m)]

        def dfs(root, depth, start, end):
            if not root:
                return
            mid = start + (end - start) // 2
            res[depth][mid] = str(root.val)
            dfs(root.left, depth + 1, start, mid - 1)
            dfs(root.right, depth + 1, mid + 1, end)


        dfs(root, 0, 0, n)
        return res