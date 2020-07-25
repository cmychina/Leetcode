#递归
def isSameTree(p, q):
    if  p==q:
        return True
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

#迭代
def isSameTree(p, q):
    stack = [(q, p)]
    while stack:
        a, b = stack.pop()
        if not a and not b:
            continue
        if a and b and a.val == b.val:
            stack.append((a.left, b.left))
            stack.append((a.right, b.right))
        else:
            return False
    return True