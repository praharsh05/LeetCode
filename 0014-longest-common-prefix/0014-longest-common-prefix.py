class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        res_len = len(res)

        for s in strs[1:]:
            while res != s[:res_len]:
                res_len -= 1
                if res_len == 0:
                    return ""

                res = res[:res_len]
        
        return res