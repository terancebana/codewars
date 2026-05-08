# Kata: Find the missing letter
# Rank: 6 kyu
# Solved: 2026-05-08
# Source: https://www.codewars.com/kata/find-the-missing-letter
# -----------------------------------------------

def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i + 1]) - ord(chars[i]) != 1:
            return chr(ord(chars[i]) + 1)