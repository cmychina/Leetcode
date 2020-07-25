"""
对于所有的主对角线有 行号 + 列号 = 常数，对于所有的次对角线有 行号 - 列号 = 常数.
"""
#O（N!）
class Solution:
    def solveNQueens(self, n: int):
        res = []
        if n == 0:
            return res
        nums = [i for i in range(n)]
        col = set()
        master = set()
        slave = set()
        stack = []
        def backtrack( nums, row,  col, master, slave, stack, res):
            #行
            if row == n:
                board = convert2board(stack)
                res.append(board)
                return
            #列
            for i in range(n):
                if i not in col and row  + i not in master and row - i not in slave: ##关键点
                    stack.append(nums[i])
                    col.add(i)
                    master.add(row + i)
                    slave.add(row - i)
                    backtrack(nums, row + 1,  col, master, slave, stack, res)
                    slave.remove(row - i)
                    master.remove(row + i)
                    col.remove(i)
                    stack.pop()

        def convert2board( stack):
            return ["." * stack[i] + "Q" + "." * (n - stack[i] - 1) for i in range(n)]

        backtrack(nums, 0, col, master, slave, stack, res)
        return res