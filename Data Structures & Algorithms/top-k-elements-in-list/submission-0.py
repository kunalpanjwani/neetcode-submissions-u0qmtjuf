class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buff = defaultdict(int)
        
        for i in nums:
            buff[i] += 1
        sorted_buff = dict(sorted(buff.items(), key=lambda item: item[1],reverse=True))
        return list(sorted_buff.keys())[:k]
        