"""
时间复杂度O(size*N)
"""
class Solution:
    def maxInWindows(self, nums, size):
        # write code here
        if not size:
            return []
        res=[]
        N=len(nums)
        for i in range(len(nums)-size+1):
            cur=nums[i]
            for j in range(i,i+size):
                if j>=N:
                    break
                cur=max(cur,nums[j])
            res.append(cur)
        return res