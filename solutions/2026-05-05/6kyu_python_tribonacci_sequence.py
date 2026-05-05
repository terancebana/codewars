# Kata: Tribonacci Sequence
# Rank: 6 kyu
# Solved: 2026-05-05
# Source: https://www.codewars.com/kata/tribonacci-sequence
# -----------------------------------------------

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(3, n):
        res.append(sum(res[-3:]))
    return res