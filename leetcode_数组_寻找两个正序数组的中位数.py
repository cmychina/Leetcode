"""
这道题如果时间复杂度没有限定在 O(log(m+n))O(log(m+n))，
我们可以用 O(m+n)O(m+n) 的算法解决，用两个指针分别指向两个数组，比较指针下的元素大小，一共移动次数为 (m+n + 1)/2，便是中位数。

num1: [a1,a2,a3,...an]
nums2: [b1,b2,b3,...bn]
[nums1[:left1],nums2[:left2] | nums1[left1:], nums2[left2:]]
只要保证左右两边 个数 相同，中位数就在 | 这个边界旁边产生。
如何找边界值，我们可以用二分法，我们先确定 num1 取 m1 个数的左半边，那么 num2 取 m2 = (m+n+1)/2 - m1 的左半边，找到合适的 m1，就用二分法找。
当 [ [a1],[b1,b2,b3] | [a2,..an],[b4,...bn] ]
我们只需要比较 b3 和 a2 的关系的大小，就可以知道这种分法是不是准确的！


"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        left, right = 0, m
        half = (m + n + 1) // 2
        while left < right:
            i = (left + right) // 2
            j = half - i
            if nums1[i] < nums2[j - 1]:
                left = i + 1
            else:
                right = i
        i, j = left, half - left

        if i == 0:
            mid1 = nums2[j - 1]
        elif j == 0:
            mid1 = nums1[i - 1]
        else:
            mid1 = max(nums1[i - 1], nums2[j - 1])
        if (m + n) & 1:
            return mid1

        if i == m:
            mid2 = nums2[j]
        elif j == n:
            mid2 = nums1[i]
        else:
            mid2 = min(nums1[i], nums2[j])
        return (mid1 + mid2) / 2

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def findKthElement(arr1,arr2,k):
            M,N = len(arr1),len(arr2)
            if M > N:
                return findKthElement(arr2,arr1,k)
            if not arr1:
                return arr2[k-1]
            if k == 1:
                return min(arr1[0],arr2[0])
            i,j = min(k//2,M)-1,min(k//2,N)-1
            if arr1[i] > arr2[j]:
                return findKthElement(arr1,arr2[j+1:],k-j-1)
            else:
                return findKthElement(arr1[i+1:],arr2,k-i-1)
        l1,l2 = len(nums1),len(nums2)
        left,right = (l1+l2+1)//2,(l1+l2+2)//2
        return (findKthElement(nums1,nums2,left)+findKthElement(nums1,nums2,right))/2