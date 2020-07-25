class Solution:

    def minpath(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        # dp[i][j]表示到(i,j)的的最短路径值
        dp = [[0] * m for _ in range(3)]
        for j in range(1, m):
            for i in range(3):
                last_min=float("inf")
                for k in range(3):
                    last_min=min(last_min,(abs(matrix[i][j]-matrix[k][j-1])+dp[k][j-1]))
                dp[i][j] = last_min
        min_num = min(dp[0][-1], dp[1][-1], dp[2][-1])
        print(dp)
        print(min_num)

if __name__=="__main__":
    s=Solution()
    import sys
    n = int(sys.stdin.readline().strip())
    matrix=[]
    for i in range(3):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        matrix.append(values)
    s.minpath(matrix)



"""
6
5 9 5 4 4 7
4 7 4 10 3 6
2 10 9 2 3 4 
"""