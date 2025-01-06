class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an empty dict
        dict_a = {}
        freq = [[] for i in range(len(nums)+1)]
        #iterate through the list
        for num in nums:
            #count the number of occurances of a key
            if num in dict_a:
                dict_a[num] +=1
            else:
                dict_a[num] = 1
        
        #iterate through the dict and create a list with decreasing frequency
        for num,count in dict_a.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res