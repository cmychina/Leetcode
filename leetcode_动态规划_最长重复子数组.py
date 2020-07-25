class Solution:

    def findLength(self, A,B):
        n=len(A)
        m=len(B)
        dp=[[0]*(m+1) for _ in range(n+1)]
        res=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    res=max(dp[i][j],res)


        return res

if __name__=="__main__":
    s=Solution()
    A=[0, 1, 1, 1, 1]
    B=[1, 0, 1, 0, 1]
    print(s.findLength(A,B))