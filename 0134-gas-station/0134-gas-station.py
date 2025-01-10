class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # We will not be able circle back if the cost is greater than the gas available
        if sum(gas) < sum(cost): return -1

        # Now set currently available gas to 0 and starting index to 0
        curr_gas = 0
        start = 0

        # if at any point of the traversal of the gas array the difference between
        # available gas and the cost to move to the next index is negative then we won't
        # be able to move to the next index
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                # When this case arises move the start point to the next index and revert
                # the available gas to 0
                curr_gas = 0
                start = i + 1
        
        return start