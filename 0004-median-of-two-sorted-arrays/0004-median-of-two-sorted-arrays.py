class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1+nums2
        nums.sort()
        n = len(nums)
        if n%2!=0:
            return nums[n//2]
        else:
            val = n//2
            return (nums[val]+nums[val-1])/2

            