"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
"""
#1.是否存在
def hasPathSum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return hasPathSum(root.left, target - root.val) or hasPathSum(root.right, target - root.val)

#2.找到所有
def pathSum(root, sum):
    res = []
    if not root:
        return []
    def helper(root, sum, tmp):
        if not root:
            return
        if not root.left and not root.right and sum - root.val == 0 :
            tmp += [root.val]
            res.append(tmp)
            return
        helper(root.left, sum - root.val, tmp + [root.val])
        helper(root.right, sum - root.val, tmp + [root.val])
    helper(root, sum, [] )
    return res