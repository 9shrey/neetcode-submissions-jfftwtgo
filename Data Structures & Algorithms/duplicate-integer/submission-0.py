class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        return not len(n) == len(nums)