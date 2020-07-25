def maxSum(nums):
    n=len(nums)
    if not nums:
        return 0
    #dp[i]表示以i结尾的最大连续子数组的和
    dp=[0]*n
    dp[0]=nums[0]
    for i in range(1,n):
        #有一种情况是dp[i-1]<0,因此对dp[i]没有增益，所以直接取nums[i]
        dp[i]=max(nums[i],dp[i-1]+nums[i])
    return max(dp)