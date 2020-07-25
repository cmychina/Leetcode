"""
二叉搜索树的前序遍历有以下特点：
如果出现递减序列，则是左子树，否则是右子树；
右子树一定是递增的
"""
def verifyPreorder(self, preorder):
    stack = []
    new_min = float('-inf')
    for i in range(len(preorder)):
        if preorder[i] < new_min:
            return False
        while stack and preorder[i] > stack[-1]:
            new_min = stack.pop()
        stack.append(preorder[i])
    return True