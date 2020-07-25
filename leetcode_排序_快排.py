
class solution:
    def quicksort(self,nums,left,right):
        if left<right:
            mid=self.partition(nums,left,right)
            left=self.quicksort(nums,left,mid-1)
            right=self.quicksort(nums,mid+1,right)
        return nums

    def partition(self,nums,left,right):
        tmp=nums[left]
        while left<right:
            #只要右边right都大于tmp,就移动right指针
            while left<right and nums[right]>tmp:
                right-=1
            #找到第一个小于tmp的值
            nums[left]=nums[right]
            while left<right and nums[left]<tmp:
                left+=1
            nums[right]=nums[left]
        nums[left]=tmp
        return left

if __name__ == "__main__":
    s = solution()
    nums=[2,1,3,4,9,8,5,6]
    print(s.quicksort(nums,0,len(nums)-1))