class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = "".join(char for char in s if char.isalnum())
        lowered = new_s.lower()
        print(lowered)

        for i in range(len(lowered)):  #0 - 18 indices
            first = lowered[i] #0
            last = lowered[len(lowered) - 1 - i]

            if first != last:
                return False
        return True



        