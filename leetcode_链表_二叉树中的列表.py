class Solution:
    """
    类似于A是B的子树
    """
    def isSubPath(self, head, root) -> bool:
        if not root:
            return False
        return self.helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def helper(self, head, root):
        if not head:
            return True
        if root and root.val != head.val or not root:
            return False
        return self.helper(head.next, root.left) or self.helper(head.next, root.right)

class Solution:
    def isSubPath(self, head, root) -> bool:
        if not head or not root:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == head.val:
                res = self.find(head, node)
                if res:
                    return res
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def find(self, head, root):
        if head.val != root.val:
            return False
        if not head.next:
            return True
        if root.left and root.right:
            return self.find(head.next, root.left) or self.find(head.next, root.right)
        elif root.left:
            return self.find(head.next, root.left)
        elif root.right:
            return self.find(head.next, root.right)
        else:
            return False



