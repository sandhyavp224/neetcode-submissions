class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}
        ans = []
        for word in strs:
            key = tuple(sorted(word))
            freq[key] = freq.get(key ,[]) + [word]
        for k , v in freq.items():
            ans.append(v)
        return ans
        