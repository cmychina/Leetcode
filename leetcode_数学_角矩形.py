class Solution:
    def countCornerRectangles(self, grid):
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row - 1):
            one = []
            for k in range(col):
                if grid[i][k] == 1:
                    one.append(k)
            #print(one)
            #算每行一的个数，然后将1的列值记录，再从之后的行中判断是否存在这样的1
            #最后使用公式计算矩形个数
            for j in range(i+1, row):
                tmp = 0
                for t in one:
                    if grid[j][t] == 1:
                        tmp += 1
                res += tmp * (tmp - 1) // 2
        return res