class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = []
        count = 0
        for i, num in enumerate(nums):

            if num not in seen:
                seen.append(num)  #seen = [1, 2, 3, 4]
            elif num in seen:
                return True
        return False



        