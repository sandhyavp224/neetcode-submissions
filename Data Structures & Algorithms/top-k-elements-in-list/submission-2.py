class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num , 0) + 1

        ans = []
        for i , v in freq.items():
            ans.append([v , i])
        ans.sort()
        res =  []
        while len(res) < k:
            res.append(ans.pop()[1])
        return res
