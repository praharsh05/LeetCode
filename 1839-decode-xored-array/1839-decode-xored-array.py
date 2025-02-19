class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for a in encoded:
            arr.append(arr[-1] ^ a)
        
        return arr