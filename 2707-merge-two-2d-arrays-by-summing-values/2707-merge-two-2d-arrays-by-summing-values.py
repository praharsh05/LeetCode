class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0
        res = []

        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 < id2:
                res.append([id1, val1])
                i += 1
            elif id1 > id2:
                res.append([id2, val2])
                j += 1
            else:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
        
        while i < n:
            res.append(nums1[i])
            i += 1
        
        while j < m :
            res.append(nums2[j])
            j += 1
        
        return res

        