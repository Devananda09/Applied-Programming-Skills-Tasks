class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = nums1+nums2
        nums1.sort()
        n = len(nums1)
        if n%2!=0:
            return nums1[n//2]
        else:
            val = n//2
            return (nums1[val]+nums1[val-1])/2

            