class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Dictionary to store how many times each product appears
        product_dict = defaultdict(int)

        # Interate over each element in the array
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # Compute the product and store it in the dict
                prod = nums[i] * nums[j]
                product_dict[prod] += 1
        
        total = 0
        # Count valid tuples based on frequency
        for count in product_dict.values():
            if count >= 2:
                # each count contributes count * (count-1) // 2 unique pair
                total += count * (count-1) // 2
        # Each unique pair can be arranged in 8 different ways so total * 8
        return total * 8