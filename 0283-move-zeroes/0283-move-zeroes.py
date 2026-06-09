class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(0)
        return nums
        