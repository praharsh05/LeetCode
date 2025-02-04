class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in wordList: return 0

        # BFS approach
        q = deque([(beginWord, 1)])
        
        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            for i in range(len(word)):
                original = word[i]
                for ch in range(26):
                    transformed = word[:i] + chr(ord('a') + ch) + word[i+1:]
                    if transformed in word_set:
                        word_set.remove(transformed)
                        q.append((transformed, steps+1))
        
        return 0