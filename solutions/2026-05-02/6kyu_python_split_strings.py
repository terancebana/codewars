# Kata: Split Strings
# Rank: 6 kyu
# Solved: 2026-05-02
# Source: https://www.codewars.com/kata/split-strings
# -----------------------------------------------

def solution(s):
    if len(s) % 2:
        s += '_'
    return [s[i:i+2] for i in range(0, len(s), 2)]