class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        res = []

        def preorder(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        d = iter(data.split(","))

        def helper():
            tmp = next(d)
            if tmp == "#":
                return
            node = TreeNode(int(tmp))
            node.left = helper()
            node.right = helper()
            return node

        return helper()