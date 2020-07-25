class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n=len(nums)
        count=0
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                cur=nums[i]+nums[j]+nums[k]
                if cur>=target:
                    k=k-1
                if cur<target:
                    count+=k-j
                    j+=1
        return count