# Kata: Pascal's Triangle
# Rank: 6 kyu
# Solved: 2026-05-11
# Source: https://www.codewars.com/kata/pascals-triangle
# -----------------------------------------------

def pascals_triangle(n):
    result = []
    row = [1]
    for _ in range(n):
        result.extend(row)
        row = [1] + [row[i] + row[i+1] for i in range(len(row) - 1)] + [1]
    return result