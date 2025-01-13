class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]
        print(rows)
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        print(rows)
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        print(rows)

        return ''.join(rows)