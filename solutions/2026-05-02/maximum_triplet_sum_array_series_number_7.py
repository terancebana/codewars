# Kata: Maximum Triplet Sum (Array Series #7) 
# Rank: 7 kyu
# Solved: 2026-05-02
# Source: https://www.codewars.com/kata/maximum-triplet-sum-array-series-number-7
# -----------------------------------------------

def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])