class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}

        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1   #{'r': 2, 'a': 2, 'c': 2, 'e': 1}

        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1   #{'r': 2, 'a': 2, 'c': 2, 'e': 1}

        
        return s_map == t_map


        #1. if lengths aren't same they cant be anagrams
        #2. create empty dict that will store key as the char and value as number of times it appears for each string
        #3 
        
            


        