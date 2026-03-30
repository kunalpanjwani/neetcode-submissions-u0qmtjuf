from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        l, r = 1, max(piles)
        prev_mid = 0
        while l <= r:
            mid = (l + r)//2
            k = 0
            for i in piles:
                k += ceil(i/mid)
            if k > h:
                l = mid + 1
            if k <= h:
                r = mid - 1
                
        return l
            
            
                
