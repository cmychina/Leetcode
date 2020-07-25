# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         head=ListNode(-1)
#         p=head
#         for i in range(n):
#             p.next=ListNode(i)
#             p=p.next
#         p.next=head
#         cur=head
#         while head:
#             for i in range(m-1):
#                 cur=cur.next
#             cur.next=cur.next.next
#

# 链接：https: // www.nowcoder.com / questionTerminal / f78a359491e64a50bce2d89cff857eb6
# 来源：牛客网
#
# 约瑟夫环问题：
# 方法1：使用list模拟循环链表，用cur作为指向list的下标位置。
# 当cur移到list末尾直接指向list头部，当删除一个数后list的长度和cur的值相等则cur指向0
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        child = [i for i in range(n)]
        print(child)
        cur = 0  # 指向list的指针
        while len(child) > 1:
            for i in range(1, m):
                cur += 1
                # 当指针移到list的末尾，则将指针移到list的头
                if cur == len(child):
                    cur = 0
            # 删除一个数，此时由于删除之后list的下标随之变化
            # cur指向的便是原数组中的下一个数字，此时cur不需要移动
            child.remove(child[cur])
            if cur == len(child):  # list的长度和cur的值相等则cur指向0
                cur = 0
        return child[0]
