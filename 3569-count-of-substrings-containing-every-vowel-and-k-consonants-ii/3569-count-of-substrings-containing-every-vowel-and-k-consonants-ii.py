class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        freq = [{}, {}]
        for v in "aeiou":
            freq[0][v] = 1
        
        res, currK, vowels, extraLeft, left = 0, 0, 0, 0, 0

        for right, rightChar in enumerate(word):
            if rightChar in freq[0]:
                freq[1][rightChar] = freq[1].get(rightChar, 0) + 1
                if freq[1][rightChar] == 1:
                    vowels += 1
            else:
                currK += 1
            
            while currK > k:
                leftChar = word[left]
                if leftChar in freq[0]:
                    freq[1][leftChar] -= 1
                    if freq[1][leftChar] == 0:
                        vowels -= 1
                else:
                    currK -= 1

                left += 1
                extraLeft = 0

            while vowels == 5 and currK == k and left < right and word[left] in freq[0] and freq[1][word[left]] > 1:
                extraLeft += 1
                freq[1][word[left]] -= 1
                left += 1

            if currK == k and vowels == 5:
                res += (1+ extraLeft)

        return res 