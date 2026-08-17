class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count) #converts it to a tuple to be used as key 
            group = result[key] #if key doesn't exist it creates a list; so group = []
            group.append(word) #appends the word to the list 
        
        return list(result.values())
            
          

    

        
        