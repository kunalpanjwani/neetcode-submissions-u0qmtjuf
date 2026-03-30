class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s) or t=="":
            return ""

        window = defaultdict(int)
        freq_t = defaultdict(int)

        for i in range(len(t)):
            freq_t[t[i]] += 1

        have, need = 0, len(freq_t)
        res, reslen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in freq_t and window[c] == freq_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    have -= 1
                
                l += 1
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""

        