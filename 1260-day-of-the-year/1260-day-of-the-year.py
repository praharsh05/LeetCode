class Solution:
    def dayOfYear(self, date: str) -> int:
        dates = date.split("-")
        year = int(dates[0])
        month = int(dates[1])
        day = int(dates[2])

        leap_year = False
        month_31_days = [1, 3, 5, 7, 8, 10, 12]
        count = 0

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_year = True
        
        if month >= 2:
            for i in range(1, month):
                if i in month_31_days:
                    count += 31
                elif i == 2 and leap_year:
                    count += 29
                elif i == 2 and not leap_year:
                    count += 28
                else:
                    count += 30
        
        for i in range(1, day+1):
            count += 1
        
        return count

