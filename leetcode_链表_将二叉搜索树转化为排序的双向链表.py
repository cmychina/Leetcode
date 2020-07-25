# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        self.prev = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            # self.prev记录的是中序遍历递增的值
            # 因此对于每个root，prev表示比它小的值
            if self.prev:
                self.prev.right = root
                root.left = self.prev
            # 每次更新prev值，继续中序遍历
            self.prev = root
            dfs(root.right)

        dfs(root)
        while root.left:
            root = root.left
        # 最后这个self.prev记录的是最大值
        # 最大值再指向最小值
        self.prev.right = root
        root.left = self.prev
        return root