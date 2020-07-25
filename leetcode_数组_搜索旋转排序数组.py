class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums[left] == target else -1