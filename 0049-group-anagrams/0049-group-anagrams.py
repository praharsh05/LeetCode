class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dict
        result = defaultdict(list)

        # Iterate through strings in the list
        for string in strs:
            # create a key for a-z
            count = [0] * 26
            #iterate through the character in string
            for c in string:
                count[ord(c) - ord("a")] +=1
            
            result[tuple(count)].append(string)

        return result.values()