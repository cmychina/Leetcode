import random
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) < 1:  # 以某一概率(1/count)抽样
                    res = i
                count += 1
        return res
