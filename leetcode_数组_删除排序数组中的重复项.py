
"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
"""
class Solution:
    def removeDuplicates(self, nums):

        for i in range(len(nums)-1,0,-1):
            if nums[i]==nums[i-1]:
                nums.pop(i)
        return nums


    def remove2(self,nums):
        pre, cur = 0, 1
        while cur < len(nums):
            if nums[pre] == nums[cur]:
                nums.pop(cur)
            else:
                pre, cur = pre + 1, cur + 1
        return nums


if __name__=="__main__":
    s=Solution()
    nums=[0,0,1,1,1,2,2,3,3,4]
    print(s.remove2(nums))



