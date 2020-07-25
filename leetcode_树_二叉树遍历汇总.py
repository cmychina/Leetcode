#1.二叉树前序遍历:root-left-right
#迭代
def preorderTraversal(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res
    #另写法
    res = []
    cur = root
    stack = []
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop()
        cur=tmp.right
#递归
def preorderTraversal(root):
    res = []
    def helper(root):
        if not root:
            return
        res.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    return res

#2.二叉树中序遍历:left-root-right
#迭代
def inorderTraversal(root):
    stack=[]
    cur=root
    res=[]
    while cur or stack:
        while cur:
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        res.append(cur.val)
        cur=cur.right
    return res
#递归
def inorderTraversal(root):
    res = []
    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res

#3.二叉树后序遍历:left-right-root
#迭代
def postorderTraversal( root):
    res = []
    cur = root
    stack = []
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.right
        tmp = stack.pop()
        cur=tmp.left
    return res[::-1]
#递归
def postorderTraversal( root):
    res = []
    def helper(root):
        if not root:
            return
        helper(root.left)
        helper(root.right)
        res.append(root.val)
    helper(root)
    return res

#4.二叉树层次遍历:level-left-right
#迭代
def levelOrder(root):
    res = []
    if not root:
        return res
    level = [root]
    while level:
        res.append([node.val for node in level])
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    return res
#递归
def levelOrder(root):
   res = []
   def helper(root, depth):
        if not root:
            return
        if len(res) == depth:
            res.append([])
        res[depth].append(root.val)
        helper(root.left, depth + 1)
        helper(root.right, depth + 1)
   helper(root, 0)
   return res

#5.二叉树锯齿形层次遍历
def zigzagLevelOrder(root):
    res = []
    def helper(root, depth):
        if not root:
            return
        if len(res) == depth:
            res.append([])
        #偶数从左到右，奇数从右到左
        if depth % 2 == 0:
            res[depth].append(root.val)
        else:
            res[depth].insert(0, root.val)
        helper(root.left, depth + 1)
        helper(root.right, depth + 1)
    helper(root, 0)
    return res

#6.二叉树层次遍历逆序
#迭代
def levelOrderBottom(root):
    res = []
    def helper(root, depth):
        if not root:
            return
        if len(res) == depth:
            res.insert(0, [])
        res[-(depth+1)].append(root.val)
        helper(root.left, depth+1)
        helper(root.right, depth+1)
    helper(root, 0)
    return res
#递归
def levelOrderBottom(root):
    from collections import deque
    if not root:
        return []
    queue = deque()
    queue.appendleft(root)
    res = []
    while queue:
        tmp = []
        n = len(queue)
        for _ in range(n):
            node = queue.pop()
            tmp.append(node.val)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        res.insert(0, tmp)
    return res