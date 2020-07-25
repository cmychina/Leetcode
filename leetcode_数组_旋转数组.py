"""
先转置 再按行翻转
"""
class Solution:
    def rotate(self,matrix):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(i,m):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix
if __name__=="__main__":
    s=Solution()
    matrix =[[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print(s.rotate(matrix))