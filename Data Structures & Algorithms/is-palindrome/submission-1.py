class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            if not s[r].isalnum():
                r -= 1
            elif not s[l].isalnum():
                l += 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return s[l].lower() == s[r].lower()
