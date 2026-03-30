class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0

        for i,h in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            maxLeft = max(height[:i])
            maxRight = max(height[i+1:])

            if maxLeft > h and maxRight > h:
                totalArea += min(maxLeft,maxRight) - h
        return totalArea
                    
                