def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def minDepth(self, root):
    if not root:
        return 0
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    return left + right + 1 if (left==0 or right==0) else min(left, right) + 1

def maxDepth(root):
    from collections import deque
    if not root:
        return 0
    queue = deque()
    queue.appendleft(root)
    res = 0
    while queue:
        res += 1
        n = len(queue)
        for _ in range(n):
            tmp = queue.pop()
            if tmp.left:
                queue.appendleft(tmp.left)
            if tmp.right:
                queue.appendleft(tmp.right)
    return res