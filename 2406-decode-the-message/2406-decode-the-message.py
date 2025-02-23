class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        table = {}
        ptr = ord("a")
        for k in key:
            if k != " " and k not in table:
                table[k] = chr(ptr)
                ptr += 1
        res = ""
        for m in message:
            if m == " ": res += " "
            else: res += table[m]
        
        return res