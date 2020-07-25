class Solution:
    def addOperators(self, num: str, target: int):

        if not num:
            return []
        result = []
        make = ['', '+', '-', '*']

        def trackback(nums, i, item):
            if i == len(nums) - 1:
                if eval(item) == target:
                    result.append(item)
                return
            if i == 0:
                item = nums[0]

            for m in make:
                if item[-1] == '0' and m == '':
                    continue
                trackback(nums, i+1, item+ m + nums[i+1])

        trackback(num, 0, '')
        return result