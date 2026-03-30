class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            nxt = 0
            for j in temperatures[i:]:
                if j > temperatures[i]:
                    res.append(nxt)
                    break
                else:
                    nxt+=1
            if len(res) != i + 1:
                res.append(0)
        return res
            