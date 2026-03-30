class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        for i,h in enumerate(heights):
            left,right = 0,0
            l=i-1
            r=i+1
            while l>=0 and heights[l]>=h:
                left+=1
                l-=1
            while r<len(heights) and heights[r]>=h:
                right+=1
                r+=1
            stack.append(h*(right+left+1))
        return max(stack)