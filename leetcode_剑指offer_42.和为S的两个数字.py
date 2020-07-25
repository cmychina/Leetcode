"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        i=0
        j=len(array)-1
        res=[]
        while i<j:
            cur=array[i]+array[j]
            if cur==tsum:
                res.append([array[i],array[j],array[i]*array[j]])
                i+=1
                j-=1
            elif cur<tsum:
                i+=1
            else:
                j-=1
        if not res:
            return []
        res.sort(key=lambda x:x[-1])
        ans=[i[0:-1] for i in res]
        return ans[0]


if __name__=="__main__":
    s=Solution()
    numbers=[1,2,4,7,11,16]
    t=10
    print(s.FindNumbersWithSum(numbers,t))