"""
先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
再找出另一个最大索引 l 满足 nums[l] > nums[k]；
交换 nums[l] 和 nums[k]；
最后翻转 nums[k+1:]
"""
class Solution:
    def nextPermutation(self, nums):
        firstIndex = -1
        n = len(nums)

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        #先找出最大的索引 k 满足 nums[k] < nums[k+1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstIndex = i
                break
        #如果不存在，就翻转整个数组
        if firstIndex == -1:
            reverse(nums, 0, n - 1)
            return
        #再找出另一个最大索引 l 满足 nums[l] > nums[k]
        secondIndex = -1
        for i in range(n - 1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex + 1, n - 1)
        return nums

if __name__ == "__main__":
    s = Solution()
    nums=[1,2,4,3]
    print(s.nextPermutation(nums))