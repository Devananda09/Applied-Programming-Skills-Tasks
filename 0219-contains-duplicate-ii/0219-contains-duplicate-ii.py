class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        ind_set = {}
        for i in range(len(nums)):
            if nums[i] in ind_set:
                if i-ind_set[nums[i]]<=k:
                    return True
            ind_set[nums[i]] = i
        return False
        
        