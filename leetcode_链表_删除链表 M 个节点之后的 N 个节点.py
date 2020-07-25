class Solution:
    def deleteNodes(self, head, m: int, n: int):

        p = head
        while p and p.next:
            for i in range(m - 1):
                if p.next:
                    p = p.next
                else:
                    break
            cur = p
            for j in range(n):
                if cur and cur.next:
                    cur = cur.next
                else:
                    break
            p.next = cur.next
            p = p.next

        return head