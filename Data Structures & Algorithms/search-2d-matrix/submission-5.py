class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l, r = 0, m - 1

        while l <= r:
            mid = (l + r)//2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        
        if l>r:
            return False
        
        l, r = 0, n - 1
        
        while l <= r:
            m = (l+r)//2
            if target < matrix[mid][m]:
                r = m - 1
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                return True
        return False
