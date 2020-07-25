"""
从前序与中序遍历序列构造二叉树,从中序与后序遍历序列构造二叉树，根据前序和后序遍历构造二叉树
"""
class TreeNode:
    pass
#1.从前序与中序遍历序列构造二叉树
def buildTree(preorder, inorder) -> TreeNode:
    if len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root

#2.从中序与后序遍历序列构造二叉树
def buildTree(inorder, postorder):
    if len(inorder)==0:
        return None
    root=TreeNode(postorder[-1])
    mid=inorder.index(postorder[-1])
    root.left=buildTree(inorder[:mid],postorder[:mid])
    root.right=buildTree(inorder[mid+1:],postorder[mid:-1])
    return root