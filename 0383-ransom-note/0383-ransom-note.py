class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Hash table for magazine
        maga_hash = {}

        # Iterate over magazine and save the count of each char to the hash table
        for c in magazine:
            maga_hash[c] = 1 + maga_hash.get(c, 0)

        # Iterate over each char in ransomNote
        for c in ransomNote:
            # if the char in ransomNote is absent in hash table or the count of the char
            # becomes 0 return false else subtract 1 from the visted char in hash table
            if c not in maga_hash or maga_hash[c] <= 0:
                return False
            maga_hash[c] -= 1
        
        return True
        