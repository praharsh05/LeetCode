class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the full word if this is an end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildTrie():
            """Builds a Trie from the given list of words."""
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.word = word  # Mark the end of a word
            return root
        
        def dfs(r, c, node):
            """Performs DFS on the board to find words in the Trie."""
            char = board[r][c]
            if char not in node.children:
                return  # No matching prefix, stop searching
            
            next_node = node.children[char]
            if next_node.word:  # Found a valid word
                found_words.add(next_node.word)
                next_node.word = None  # Avoid duplicate additions

            # Mark as visited
            board[r][c] = "#"

            # Explore neighbors (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node.children:
                    dfs(nr, nc, next_node)

            # Restore board state (backtracking)
            board[r][c] = char

            # Optimization: Remove leaf nodes to reduce Trie size
            if not next_node.children:
                del node.children[char]

        # Step 1: Build Trie
        trie_root = buildTrie()
        rows, cols = len(board), len(board[0])
        found_words = set()

        # Step 2: Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie_root.children:
                    dfs(r, c, trie_root)

        return list(found_words)