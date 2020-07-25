class Solution:
    def generateMatrix(self, n):

        # 螺旋矩阵
        nums = [i + 1 for i in range(n ** 2)]
        dx = 0
        dy = 1
        i = 0
        j = 0
        matrix = [[0] * n for _ in range(n)]
        for z in range(n ** 2):
            matrix[i][j] = nums[z]
            if matrix[(i + dx) % n][(j + dy) % n] != 0:
                dx, dy = dy, -dx

            i += dx
            j += dy

        return matrix