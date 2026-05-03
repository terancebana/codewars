# Kata: Ordered Count of Characters
# Rank: 7 kyu
# Solved: 2026-05-03
# Source: https://www.codewars.com/kata/ordered-count-of-characters
# -----------------------------------------------

from collections import Counter

def ordered_count(inp):
    return list(Counter(inp).items())