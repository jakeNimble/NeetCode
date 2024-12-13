class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMaps = {}
        for num in nums:
            if num in numMaps:
                return True
            else:
                numMaps[num] = 1
        return False