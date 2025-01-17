class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dict
        res = defaultdict(list)

        # Iterate through strings in the list
        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)

        return list(res.values())