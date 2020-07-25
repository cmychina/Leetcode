class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class convert:
    def list2link(li):
        n=len(li)
        ans=ListNode(-1)
        cur=ans
        for i in range(n):
            cur.next=ListNode(li[i])
            cur=cur.next
        return ans.next

    def link2list(li):
        ans=[]
        while li:
            ans.append(li.val)
            li=li.next
        return ans

    def tree2list(node):
        res=[]
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        return res








