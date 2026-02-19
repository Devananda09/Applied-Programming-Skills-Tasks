class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        
        while stack:
            next_greater[stack.pop()] = -1

        
        ans = []
        for num in nums1:
            ans.append(next_greater[num])

        return ans
