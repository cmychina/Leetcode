class Solution:
    def findLength(self, A, B) :
        dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
        res=0
        ans=''
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                    if dp[i+1][j+1]>res:
                        res=dp[i+1][j+1]
                        flag=i+1

        return A[flag-res:flag]

    def Mundane(self, A, B) :
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    res = max(dp[i + 1][j + 1], res)
        return res


if __name__=="__main__":
    s=Solution()
    A=[1, 2, 3, 2, 1]
    B=[3, 2, 1, 4, 7]
    print(s.Mundane(A,B))