"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为0。请使用原地算法。
"""
class Solution:

    def setZero(self,matrix):
        n=len(matrix)
        m=len(matrix[0])
        zero=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    zero.append((i,j))

        def set2Zero(matrix,point):
            x = point[0]
            y = point[1]
            for j in range(m):
                matrix[x][j] = 0
            for i in range(n):
                matrix[i][y] = 0
            return matrix

        for point in zero:
            matrix=set2Zero(matrix,point)

        return matrix





if __name__=="__main__":
    s=Solution()
    matrix=[[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
    print(s.setZero(matrix))


