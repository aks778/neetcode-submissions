class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        lookup = {}
        if len(s) != len(t):
            return False

        for letter in s:
            lookup[letter] = lookup.get(letter, 0) + 1

        for letter in t:
            if letter in lookup:
                lookup[letter] -= 1
            
                if lookup[letter] < 0:
                    return False
            else:
                return False
        return True
        
            
        
        

        