class Solution:
    def dayOfYear(self, date: str) -> int:
        dates = date.split("-")
        year, month, day = map(int, dates)

        # Days in each month for normal years
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check if it's a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29  # February has 29 days in leap year

        # Sum the days in previous months and add current day
        return sum(days_in_month[:month - 1]) + day