class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lng = defaultdict(list)
        for i in sorted(nums):
            if lng[i] != []:
                continue
            lng[i].append(i)
            for j in sorted(nums):
                if j==lng[i][-1]+1:
                    lng[i].append(j)
                else:
                    continue
        max_len = 0
        for i in lng.values():
            if len(i)>max_len:
                max_len = len(i)
        return max_len

            
