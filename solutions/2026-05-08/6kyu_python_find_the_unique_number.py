# Kata: Find the unique number
# Rank: 6 kyu
# Solved: 2026-05-08
# Source: https://www.codewars.com/kata/find-the-unique-number
# -----------------------------------------------

def find_unique(arr):
    unique = 0
    for num in arr:
        unique ^= num
    return unique