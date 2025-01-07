class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        prev_letter = ""
        for letter in s:
            match letter:
                case "I":
                    num +=1
                case "V":
                    if prev_letter == "I":
                        num +=3
                    else:
                        num +=5
                case "X":
                    if prev_letter == "I":
                        num +=8
                    else:
                        num +=10
                case "L":
                    if prev_letter == "X":
                        num +=30
                    else:
                        num +=50
                case "C":
                    if prev_letter == "X":
                        num +=80
                    else:
                        num +=100
                case "D":
                    if prev_letter == "C":
                        num +=300
                    else:
                        num +=500
                case "M":
                    if prev_letter == "C":
                        num +=800
                    else:
                        num +=1000

            prev_letter = letter
        
        return num