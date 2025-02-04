class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            # If a char of word does not exist in the children of the node then add it to the children
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move the current node to the children node
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        # Start from the trie root
        curr = self.trie
        for char in word:
            if char not in curr.children: return False

            # Move to child node
            curr = curr.children[char]
        
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr.children: return False

            curr = curr.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)