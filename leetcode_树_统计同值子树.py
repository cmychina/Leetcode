"""
给定树中的一个结点，若其满足下面条件中的一个，则子树同值:
该节点没有子结点 （基本情况）
该节点的所有子结点都为同值子树，且结点与其子结点值相同。
"""
class S:
    def countUnivalSubtrees(self, root):
        self.res = 0

        def helper(root, val):
            if not root:
                return True
            left = helper(root.left, root.val)
            right = helper(root.right, root.val)
            #left和right没有子节点 或者左右子树有同值子树且val相等
            if left == right == True:
                self.res += 1
            else:
                return False
            return root.val == val

        root and helper(root, root.val)
        return self.res