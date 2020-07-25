class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class  Solution:
    def buildTree(self,inorder, postorder):
        if len(inorder)==0:
            return None
        root=TreeNode(postorder[-1])
        mid=inorder.index(postorder[-1])
        root.left=self.buildTree(inorder[:mid],postorder[:mid])
        root.right=self.buildTree(inorder[mid+1:],postorder[mid:-1])
        return root
