class Solution:
    def convertDateToBinary(self, date: str) -> str:
        strings = date.split("-")
        res = []
        for string in strings:
            res.append(str(bin(int(string))).replace('0b', ''))
        
        return "-".join(res)