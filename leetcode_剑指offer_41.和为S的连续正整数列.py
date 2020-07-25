"""
很快的找出所有和为S的连续正数序列
思路：连续正数一定是等差
(a1+an)*n/2=t
an=a1+(n-1)d
d=1
2a1+n-1=2t
2a1=2t+1-n
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        tmp=2*tsum
        cur=tsum//2
        res=[]
        for a1 in range(tsum):
            for n in range(tsum):
                if (2*a1+n-1)*n==tmp:
                    res.append((a1,n))
        ans=[]
        for i in res:
            a1=i[0]
            if a1==0:
                continue
            n=i[1]
            c=[a1+i for i in range(n)]
            ans.append(c)
        return ans

if __name__=="__main__":
    s=Solution()
    print(s.FindContinuousSequence(15))

