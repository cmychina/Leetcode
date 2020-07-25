"""
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
"""
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack,hash=[],{}
        for i in nums2:
            while stack and stack[-1]<i:
                hash[stack.pop()]=i
            stack.append(i)
        return [hash.get(i,-1) for i in nums1]

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        res=[-1]*n
        for i in range(2*n):
            while stack and nums[stack[-1]]<nums[i%n]:
                res[stack[-1]]=nums[i%n]
                stack.pop()
            stack.append(i%n)
        return res