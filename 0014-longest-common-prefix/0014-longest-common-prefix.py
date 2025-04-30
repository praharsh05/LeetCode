class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        base_len = len(base)

        for string in strs[1:]:
            while string[:base_len] != base:
                if base_len == 0:
                    return ""
                base_len -= 1

                base = base[:base_len]
        
        return base