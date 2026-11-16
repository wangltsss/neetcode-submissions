class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        return len(set(nums)) != n