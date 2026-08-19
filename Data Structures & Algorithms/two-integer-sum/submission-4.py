class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mpp = {}
        for i , v in enumerate(nums):
            diff = target - v
            if diff in mpp:
                return [mpp[diff] , i]
            mpp[v] = i