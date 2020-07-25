"""
给定一个包含红色、白色和蓝色，一共 n个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
"""
class Solution:
    def sortColors(self, nums) -> None:
        p0 = cur = 0
        p2 = len(nums) - 1
        while cur <= p2:
            if nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur+= 1