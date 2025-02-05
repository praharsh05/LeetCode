# TrieNode class with a dictionary of children and a flag for end of word
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start at the root node
        curr = self.root
        # Iterate over each character of the word and build the trie
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        
        curr.is_word = True
    

    def search(self, word: str) -> bool:
        # DFS with back backtracking
        def dfs(node: TrieNode, index: int):
            if index == len(word): return node.is_word

            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1): return True
            
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)