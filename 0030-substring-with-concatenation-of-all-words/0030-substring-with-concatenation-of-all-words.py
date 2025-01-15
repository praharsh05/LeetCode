from collections import defaultdict, deque
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []

        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        word_len = len(words[0])
        sub_str_len = len(words) * word_len
        
        res = []

        for i in range(word_len):
            queue = deque()
            word_dict = word_count.copy()
            for j in range(i, len(s) - word_len +1, word_len):
                word = s[j: j+word_len]
                if word_dict.get(word, 0) != 0:
                    word_dict[word] -= 1
                    queue.append(word)
                    if sum(word_dict.values()) == 0:
                        res.append(j - sub_str_len + word_len)
                        last_element = queue.popleft()
                        word_dict[last_element] = word_dict.get(last_element, 0) + 1
                else:
                    while len(queue):
                        last_element = queue.popleft()
                        if last_element == word:
                            queue.append(word)
                            break
                        else:
                            word_dict[last_element] = word_dict.get(last_element, 0) +1
                            if word_dict[last_element] > word_count[last_element]:
                                word_dict = word_count.copy()

        
        return res