class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seive = [True] * (right + 1)
        seive[0] = seive[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if seive[i]:
                for j in range(i * i, right + 1, i):
                    seive[j] = False
        
        primes = [i for i in range(left, right + 1) if seive[i]]

        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        res = [-1, -1]

        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < min_gap:
                min_gap = gap
                res = [primes[i-1], primes[i]]
        
        return res