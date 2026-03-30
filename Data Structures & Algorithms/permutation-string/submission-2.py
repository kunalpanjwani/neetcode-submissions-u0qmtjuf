class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq_s1 = defaultdict(int)
        for i in s1:
            freq_s1[i] += 1
        
        win = len(s1)
        
        l = 0
        r = len(s1)
        while r <= len(s2):
            freq_s2 = defaultdict(int)
            for c in s2[l:r]:
                freq_s2[c] += 1
            print(freq_s2)
            if freq_s2 == freq_s1:
                return True
            else:
                l += 1
                r += 1
        return False


