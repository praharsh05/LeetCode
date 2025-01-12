class Solution:
    def intToRoman(self, num: int) -> str:
        rstr = ""
        if num // 1000 >= 1:
            th = num // 1000
            if th <= 3:
                for i in range(1, th+1):
                    rstr += "M"
            num %= 1000
        if num // 100 >= 1:
            hr = num // 100
            if hr <= 3:
                for i in range(1, hr+1):
                    rstr += "C"
            if hr == 4:
                rstr += "CD"
            if hr >= 5 and hr != 9:
                rstr += "D"
            if hr > 5 and hr < 9:
                m5 = hr - 5
                for i in range(1, m5+1):
                    rstr += "C"
            if hr == 9:
                rstr += "CM"
            num %= 100
        if num // 10 >= 1:
            tn = num // 10
            if tn <= 3:
                for i in range(1, tn+1):
                    rstr += "X"
            if tn == 4:
                rstr += "XL"
            if tn >= 5 and tn != 9:
                rstr += "L"
            if tn > 5 and tn < 9:
                m5 = tn - 5
                for i in range(1, m5+1):
                    rstr += "X"
            if tn == 9:
                rstr += "XC"
            num %= 10
        if num // 1 >= 1:
            one = num // 1
            if one <= 3:
                for i in range(1, one+1):
                    rstr += "I"
            if one == 4:
                rstr += "IV"
            if one >= 5 and one != 9:
                rstr += "V"
            if one > 5 and one < 9:
                m5 = one - 5
                for i in range(1, m5+1):
                    rstr += "I"
            if one == 9:
                rstr += "IX"
        
        return rstr
            