class TreeNode:
    pass
#1.暴力法
def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

#没有用到完全二叉树性质


#2.
# 二分查找
# // 最后一层的叶子节点全部靠向左边，我们可以用二分搜索只检查
# log(2 ^ d) = d个叶子代替检查全部叶子。
# // idx为想要去确定是否存在的节点



def exists(self, idx: int, d: int, node: TreeNode) -> bool:
    left, right = 0, 2 ** d - 1
    for _ in range(d):
        pivot = left + (right - left) // 2
        if idx <= pivot:
            node = node.left
            right = pivot
        else:
            node = node.right
            left = pivot + 1
    return node is not None


def countNodes(self, root: TreeNode) -> int:
    if not root:
        return 0
    #树的深度
    d = 0
    while node.left:
        node = node.left
        d += 1
    if d == 0:
        return 1
    #判断最后一层节点数
    left, right = 1, 2 ** d - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if self.exists(pivot, d, root):
            left = pivot + 1
        else:
            right = pivot - 1
    return (2 ** d - 1) + left
