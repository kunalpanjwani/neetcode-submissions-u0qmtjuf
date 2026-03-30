class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,val in enumerate(temperatures):
            if i==0:
                stack.append(val)
                continue
            j=i-1
            while j>=0 and stack and val > temperatures[j]:
                print(j)
                if res[j] == 0:
                    res[j] = i-j
                j-=1
        return res 
            