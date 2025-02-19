class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        def count_word(string):
            s = string.split(" ")
            return len(s)
        
        maximum = 0

        for sentence in sentences:
            maximum = max(count_word(sentence), maximum)
        
        return maximum