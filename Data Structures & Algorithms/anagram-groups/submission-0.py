class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        buff = defaultdict(list)
        
        for i, val in enumerate(strs):
            k = ''.join(sorted(val))
            
            buff[k].append(strs[i])
        
        return list(buff.values())