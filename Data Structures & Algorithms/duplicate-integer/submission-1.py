class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = {}
        for num in nums:
            if num in mapper:
                return True 
            else:
                mapper[num] = 1

        return False
