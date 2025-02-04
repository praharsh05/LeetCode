class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert the list to set for faster lookup
        word_set = set(wordList)
        # If endWord is not present in word_set then return 0 as it is impossible wo reach endWord
        if endWord not in word_set: return 0

        # BFS approach
        q = deque([(beginWord, 1)])
        
        while q:
            word, steps = q.popleft()
            # if we reach the endWord return steps
            if word == endWord:
                return steps
            # Iterate over each character of word
            for i in range(len(word)):
                original = word[i]
                # Iterate over each characte from a to z to check for transformed word in word_set
                for ch in range(26):
                    transformed = word[:i] + chr(ord('a') + ch) + word[i+1:]
                    # If transformed in word set then remove it from word set and append
                    # it to the q with steps + 1
                    if transformed in word_set:
                        word_set.remove(transformed)
                        q.append((transformed, steps+1))
        
        return 0