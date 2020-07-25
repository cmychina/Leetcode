"""
给定一个整数n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
给定一个整数n，生成所有由 1 ... n为节点所组成的二叉搜索树。
1.BST种类
思路:遍历每个i, 1~i-1构成左子树，i+1~n构成右子树。
G(n)表示长度为n的序列的不同BST个数
F(i,n)表示以i为为根的不同BST个数
G(n)=∑F(i,n) i=1,2,3~n
F(i,n)=G(i-1)G(n-i)
G(n)=∑G(i-1)G(n-i)

"""
#dp即可
def numTrees(n):
    G = [0]*(n+1)
    G[0], G[1] = 1, 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] += G[j-1] * G[i-j]
    return G[n]

#2.生成BST
def generateTrees(n):
    if n==0:
        return []
    def helper(left, right):
        res=[]
        if left > right:
            return [None]
        for i in range(left, right+1):
            left_trees=helper(left, i-1)
            right_trees=helper(i+1, right)
            for l in left_trees:
                for r in right_trees:
                    cur=TreeNode(i)
                    cur.left=l
                    cur.right=r
                    res.append(cur)
        return res
    return helper(1,n)