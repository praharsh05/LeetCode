class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_freq_ran, letter_freq_mag = {}, {}
        for letter in ransomNote:
            if letter in letter_freq_ran:
                letter_freq_ran[letter] += 1
            else:
                letter_freq_ran[letter] = 1
        print(letter_freq_ran) 

        for letter in magazine:
            if letter in letter_freq_mag:
                letter_freq_mag[letter] += 1
            else:
                letter_freq_mag[letter] = 1
        print(letter_freq_mag)

        for letter in letter_freq_ran:
            if letter not in letter_freq_mag: return False
            if letter_freq_ran[letter] > letter_freq_mag[letter]:
                return False
        
        return True
        