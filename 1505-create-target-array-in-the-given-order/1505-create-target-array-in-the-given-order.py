class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(nums)):
            print(target)
            if index[i] > len(target)-1:
                target.append(nums[i])
            else:
                temp = target[index[i]:]
                target[index[i]] = nums[i]
                j = index[i] + 1
                for k in range(len(temp)):
                    if j > len(target) -1:
                        target.append(temp[k])
                        j += 1
                    else:
                        target[j] = temp[k]
                        j+=1
                
        
        return target