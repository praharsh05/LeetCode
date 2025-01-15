from collections import defaultdict, deque
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Edge case if string or words list is empty
        if not s or not words: return []

        # Create a dict to store the occurance times for each word in words
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        # Variable to store Word length which is same for each word
        word_len = len(words[0])
        # Variable to store Total substring length of words
        sub_str_len = len(words) * word_len
        
        # Result array to store the occurance of substring in s
        res = []

        for i in range(word_len):
            # Queue to store the scan history
            queue = deque()
            word_dict = word_count.copy()
            for j in range(i, len(s) - word_len +1, word_len):
                # Sliding window is word
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
                            # if word_dict[last_element] exceeds the original value then reset the word_dict
                            if word_dict[last_element] > word_count[last_element]:
                                word_dict = word_count.copy()

        
        return res