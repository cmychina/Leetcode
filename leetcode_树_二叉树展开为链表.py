class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        #打平左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None

        while root.right:
            root = root.right
        root.right = tmp

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

