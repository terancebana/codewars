# Kata: Jumping  Number (Special Numbers Series  #4)
# Rank: 7 kyu
# Solved: 2026-05-02
# Source: https://www.codewars.com/kata/jumping-number-special-numbers-series-number-4
# -----------------------------------------------

def jumping_number(number):
    s = str(number)
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i+1])) != 1:
            return "Not!!"
    return "Jumping!!"