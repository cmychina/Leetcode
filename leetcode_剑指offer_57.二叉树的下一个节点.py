"""
链接：https://www.nowcoder.com/questionTerminal/9023a0c988684a53960365b889ceaf5e
1.二叉树为空，则返回空；
2.节点右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着指向左子结点的指针找到的叶子节点即为下一个节点；
3.节点不是根节点。如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, node):
        #1
        if not node:
            return None
        #2
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        #3
        while node.next:
            if node.next.left == node:
                return node.next
            node = node.next
        return None