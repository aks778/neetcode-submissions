class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = {}

        for i, n in enumerate(nums):

            difference = target - n  #4

            if difference in lookup:
                return [lookup[difference], i]
            else:
                lookup[n] = i
        
        return []

        