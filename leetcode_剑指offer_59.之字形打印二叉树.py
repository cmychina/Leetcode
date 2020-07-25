class Solution:
    def Print(self, root):
        if not root:
            return []
        stack=[root]
        res=[]
        flag=False
        while stack:
            cur_val=[]
            next_level=[]
            for node in stack:
                cur_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if flag:
                cur_val.reverse()
            if cur_val:
                res.append(cur_val)
            stack=next_level
            flag=not flag
        return res