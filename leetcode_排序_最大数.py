class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

class Solution:
    def largestNumber(self, nums) -> str:
        s=''
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
                    nums[i],nums[j]=nums[j],nums[i]
        for i in nums:
            s+=str(i)
        return str(int(s))