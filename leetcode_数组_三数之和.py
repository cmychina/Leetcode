class Solution:
    def threeSum(self,nums,target=0):
        nums.sort()
        print(nums)
        res=[]
        for i in range(len(nums)-2):
            if nums[i]>target:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>target:
                break
            elif nums[i]+nums[i+1]+nums[i+2]>target:
                break
            elif nums[i]+nums[-1]+nums[-2]<target:
                continue
            else:
                l=i+1
                r=len(nums)-1
                while l<r:
                    tmp=nums[i]+nums[l]+nums[r]
                    if tmp==target:
                        res.append([nums[i],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif tmp<target:
                        l+=1
                    else:
                        r-=1
        return res
if __name__=="__main__":
    s=Solution()
    nums =[-2,0,0,2,2]
    print(s.threeSum(nums,0))