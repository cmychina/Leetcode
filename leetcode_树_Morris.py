
class Morris:
    def preorder(root):
        if not root:
            return
        p = root;
        prenode = None
        while p:
            if p.left:
                #前驱结点的最右子节点--->自身
                prenode = p.left
                while prenode.right and prenode.right != p:
                    prenode = prenode.right
                if not prenode.right:			#建立链接方便回溯
                    print(p.val)				#打印
                    prenode.right = p
                    p = p.left
                    continue
                if prenode.right == p:
                    prenode.right = None		#回溯完成删除多余链接
            if not p.left:
                print(p.val)			#打印
            p = p.right

    def inorder(root):
        if not root: return
        p = root;
        prenode = None
        while p:
            if p.left:
                prenode = p.left
                while prenode.right and prenode.right != p:
                    prenode = prenode.right
                if not prenode.right:  # 建立链接方便回溯
                    prenode.right = p
                    p = p.left
                    continue
                #之前建立过连接，即先前结点要回溯到的父节点，打印
                if prenode.right == p:
                    print(p.val)  # 打印
                    prenode.right = None  # 回溯完成删除多余链接
            #到达最左结点，中学遍历开始打印该节点
            if not p.left:
                print(p.val)  # 打印
            p = p.right




    def Morris_preorder(self,root):
        if not root:
            return []
        p=root
        prenode=None
        res=[]
        while p:
            if p.left:
                prenode=p.left
                while prenode.right and prenode.right!=p:#还没有建立连接
                    prenode=prenode.right
                if prenode.right!=p:
                    res.append(p.val)
                    prenode.right=p
                    p=p.left
                    continue
                if prenode.right==p:
                    prenode.right=None
            if not p.left:
                res.append(p.val)
            p=p.right
        return res











