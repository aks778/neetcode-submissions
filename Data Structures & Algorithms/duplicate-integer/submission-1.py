class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = []
        count = 0
        for num in nums:

            if num not in seen:
                seen.append(num)  #seen = [1, 2, 3, 4]
            elif num in seen:
                return True
        return False



        