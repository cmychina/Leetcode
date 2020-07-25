class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        import collections
        res=[]
        def dfs(root):
            if not root:
                return
            queue=[root]
            while queue:
                ans = [node.val for node in queue]
                res.append(ans)
                nxt_queue=[]
                for node in queue:
                    if node.left:
                        nxt_queue.append(node.left)
                    if node.right:
                        nxt_queue.append(node.right)
                queue=nxt_queue
        dfs(pRoot)
        return res



