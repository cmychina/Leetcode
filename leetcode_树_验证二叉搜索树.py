"""
思路:判断中序遍历是否递增即可
"""
class Solutin:
    def isValidBST(root):
        pre=None
        stack=[]
        res=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            #pre用来表示上一个值
            if pre and pre.val>=cur.val:
                return False
            else:
                pre=cur
            cur=cur.right
        return True

    def Mundane(self, root) -> bool:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res == sorted(res) and len(set(res)) == len(res)

