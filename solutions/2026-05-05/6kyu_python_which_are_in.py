# Kata: Which are  in?
# Rank: 6 kyu
# Solved: 2026-05-05
# Source: https://www.codewars.com/kata/which-are-in
# -----------------------------------------------

def in_array(array1, array2):
    return sorted({s for s in array1 if any(s in x for x in array2)})