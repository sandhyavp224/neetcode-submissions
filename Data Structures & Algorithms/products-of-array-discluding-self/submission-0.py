class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        pref = [0] * n
        pref[0] = 1
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        
        right = 1
        for r in range(n - 1 , -1 , -1):
            pref[r] = pref[r] * right
            right *= nums[r]
        return pref
