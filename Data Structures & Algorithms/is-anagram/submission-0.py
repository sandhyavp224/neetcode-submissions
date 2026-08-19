class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}
        if len(s) != len(t):
            return False
        for c in s:
            freqs[c] = freqs.get(c , 0) + 1
        
        for c in t:
            freqt[c] = freqt.get(c , 0) + 1

        if freqt == freqs:
            return True
        return False