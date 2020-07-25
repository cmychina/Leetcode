"""
二叉搜索树中的两个节点被错误地交换。 请在不改变其结构的情况下，恢复这棵树。
这道题难点,是找到那两个交换节点,把它交换过来就行了。这两个节点有如下规律
第一个节点,是第一个按照中序遍历时候前一个节点大于后一个节点,我们选取前一个节点
第二个节点,是在第一个节点找到之后, 后面出现前一个节点大于后一个节点,我们选择后一个节点
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not firstNode and pre.val > cur.val:
                firstNode = pre
            if firstNode and pre.val > cur.val:
                secondNode = cur
            pre = cur
            cur = cur.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val


# Morris遍历
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x = y = pre = None
        while root:
           if not root.left:
              if pre and pre.val > root.val:
                 y = root
                 if x == None:
                    x = pre
              pre = root
              root = root.right
           else:
              prior = root.left
              while prior.right and prior.right != root:
                    prior = prior.right
              # 右子树链接前驱节点
              if not prior.right:
                 prior.right = root
                 root = root.left
              elif prior.right == root:
                  #当前节点错误
                   if pre and pre.val > root.val:
                      y = root
                      if x == None:
                         x = pre
                   pre = root
                   prior.right = None
                   root = root.right
        x.val,y.val = y.val,x.val
