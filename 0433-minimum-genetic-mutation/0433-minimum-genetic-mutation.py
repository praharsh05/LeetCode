class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        # Check to see if a and b are neighbors
        def check_neighbor(a: str, b: str) -> bool:
            total = 0
            for i in range(len(a)):
                if a[i] != b[i]: total += 1
            return total == 1
        
        # initialize the q with startGene and 0 mutations
        q = deque([[startGene,0]])

        # initialize the visited set with startGene
        visited = set()
        visited.add(startGene)

        while q:
            curr, mutations = q.popleft()
            if curr == endGene:
                return mutations
            # Intertate through all gene mutations in the bank
            for neighbor in bank:
                # Check if neighbor is a valid neighbor and we have visited it before, if not
                # we add it to the visited and the queue with mutations + 1
                if check_neighbor(curr, neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    q.append([neighbor, mutations+1])
        # If we dont reach the end, then there is no such mutation
        return -1