"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

"""
class Solution:
    def threeSumClosest(self,nums,target):
        res=float("inf")
        nums.sort()
        n=len(nums)
        cur=0
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                tmp=nums[i]+nums[l]+nums[r]
                if abs(tmp-target)<res:
                    res=abs(tmp-target)
                    cur=tmp
                    print(cur)

                if tmp>target:
                    r-=1
                else:
                    l+=1
        return cur




if __name__=="__main__":
    s=Solution()
    nums=[-1,2,1,-4]
    target=1
    print(s.threeSumClosest(nums,target))