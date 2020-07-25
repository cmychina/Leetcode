"""

"""
class Solution:
    def movingCount(self, threshold, rows, cols):

        M=rows
        N=cols
        cnt=0
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        self.visited=set()
        def dfs(i,j):
            if not (0<=i<M and 0<=j<N and self.isValid(i,j,threshold) and (i,j) not in self.visited):
                return 0
            self.visited.add((i,j))
            k=1
            k+=dfs(i+1,j)
            k+=dfs(i-1,j)
            k+=dfs(i,j+1)
            k+=dfs(i,j-1)
            return k
        cnt=dfs(0,0)
        return cnt

    def isValid(self,x,y,k):
        ans=0
        x=str(x)
        y=str(y)
        for i in range(len(x)):
            ans+=int(x[i])
        for j in range(len(y)):
            ans+=int(y[j])
        return ans<=k
if __name__=="__main__":
    s=Solution()
    res=s.movingCount(5,10,10)
    print(res)
