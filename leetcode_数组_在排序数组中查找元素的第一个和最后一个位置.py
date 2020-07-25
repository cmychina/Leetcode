class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1,-1]
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1
        begin=l
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        print(r)
        return [begin,r]

        #确定目标值后左右线性扫描
        length = len(nums)
        l = 0
        r = length-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                i = j =m
                while i>=0 and nums[i] == target:
                    i -= 1
                while j < length and nums[j] == target:
                    j += 1
                return [i+1,j-1]
            elif nums[m] < target:
                l =m +1
            else:
                r = m -1
        return [-1,-1]