class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # Fixed array for a-z
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the index of the char does not exist in the children of the node then add it to the children
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            # Move the current node to the child node
            curr = curr.children[index]
        curr.is_end = True

    def search(self, word: str) -> bool:
        # Start from the trie root
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]: return False

            # Move to child node
            curr = curr.children[index]
        
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not curr.children[index]: return False

            curr = curr.children[index]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)