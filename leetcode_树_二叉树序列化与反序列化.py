
class TreeNode:
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
#层次遍历
from collections import deque
class Codec:
    def serialize(self, root):
        res = []
        queue = deque()
        if root:
            queue.appendleft(root)
        while queue:
            tmp = queue.pop()
            if tmp:
                res.append(str(tmp.val))
                queue.appendleft(tmp.left)
                queue.appendleft(tmp.right)
            else:
                res.append("#")
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return
        data = iter(data.split(","))
        root = TreeNode(next(data))
        queue = deque([root])
        while queue:
            tmp = queue.pop()
            left = next(data)
            if left != "#":
                tmp.left = TreeNode(int(left))
                queue.appendleft(tmp.left)
            right = next(data)
            if right != "#":
                tmp.right = TreeNode(int(right))
                queue.appendleft(tmp.right)
        return root
