"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。调用next()将返回二叉搜索树中的下一个最小的数。
"""
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.push_stack(root)

    def next(self) -> int:
        tmp = self.stack.pop()
        if tmp.right:
            self.push_stack(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def push_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left