class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_in_time(T):
            total_cars = 0
            
            for r in ranks:
                total_cars += int((T//r) ** 0.5)

                if total_cars >= cars:
                    return True
            
            return False
        
        left = 0
        right = max(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2

            if can_repair_in_time(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

