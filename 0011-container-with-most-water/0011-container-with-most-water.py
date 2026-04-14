class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        max_h2o=0
        while i<j:
            width = j-i
            water_hight = min(height[i],height[j])
            area = width*water_hight
            max_h2o=max(max_h2o,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_h2o
        