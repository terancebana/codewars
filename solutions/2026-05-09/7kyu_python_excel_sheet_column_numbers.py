# Kata: Excel sheet column numbers
# Rank: 7 kyu
# Solved: 2026-05-09
# Source: https://www.codewars.com/kata/excel-sheet-column-numbers
# -----------------------------------------------

def title_to_number(title):
    res = 0
    for char in title:
        res = res * 26 + ord(char) - 64
    return res