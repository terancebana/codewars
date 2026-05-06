# Kata: Chain me
# Rank: 7 kyu
# Solved: 2026-05-06
# Source: https://www.codewars.com/kata/chain-me
# -----------------------------------------------

def chain(input, fs):
    for f in fs:
        input = f(input)
    return input