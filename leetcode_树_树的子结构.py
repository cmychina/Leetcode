class Solution:
    def isSubStructure(self, A, B) -> bool:

        def isSameTree(t1,t2):
            if not t2:
                return True
            if not t1 or t1.val!=t2.val:
                return False
            return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

        if not A:
            return False
        if not B:
            return False

        return isSameTree(A,B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)