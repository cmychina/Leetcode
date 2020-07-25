class Solution:
    #def longestPalindrome(self,s):
    #dp[i][j]表示s[i][j]是否为回文子串?
    def dp(self,s):
        n=len(s)
        res=""
        max_len=float("-inf")
        dp=[[0]*n for _ in range(n)]
        #任何一个单字母都是回文串
        for i in range(n):
            dp[i][i]=1
        for i in range(1,n):
            for j in range(i,-1,-1):
                if s[i]==s[j] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i]=1
                if dp[j][i] and max_len<i-j+1:
                    res=s[j:i+1]
                    max_len=i+1-j
        return res




    def centerSpread(self,s):
        n=len(s)
        self.res = 0
        self.ans=""
        def helper(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            #self.res=max(self.res,j-i-1)
            if j-i-1>self.res:
                self.res=j-i-1
                self.ans=s[i+1:j]

        for i in range(n-1):
            helper(i,i)
            helper(i,i+1)
        print(self.res)
        return self.ans

    def Mundane(self,s):
        n=len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i,-1,-1):
                if s[i]==s[j] or (i-j<=2 or dp[j+1][i-1]==True):
                    dp[j][i]=True

if __name__=="__main__":
    s=Solution()
    st="abababa"
    print(s.centerSpread(st))