class Solution:
    def generate(self, numRows):
        res=[]
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                res[i].append(1)
        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
