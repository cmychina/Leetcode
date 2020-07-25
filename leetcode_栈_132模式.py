class Solution:
    def find132pattern(self, nums):

        stack = []
        m = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < m:
                return True
            while stack and nums[i] > stack[-1]:
                m = stack.pop()
                print("m",m)
            stack.append(nums[i])
            print(stack)

        return False
if __name__ == "__main__":
    s = Solution()
    nums=[1,2,3,2,0]
    print(s.find132pattern(nums))