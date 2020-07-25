"""
序列化时通过某种符号表示空节点（#），以！表示一个结点值的结束（value!）。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        self.res=''
        def dfs(root):
            if not root:
                return '#'
            self.res+=str(root.val)
            self.res+='!'
            dfs(root.left)
            self.res+='!'
            dfs(root.right)

    def Deserialize(self, s):
        self.flag += 1
        l = s.split('!')
        if self.flag >= len(s):
            return None
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root