class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}

        for name, height in zip(names, heights):
            dic[height] = name
        
        return [v for k, v in sorted(dic.items(), key=lambda item: item[0], reverse=True)]
        
