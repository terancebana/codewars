# Kata: Euclidean distance in n dimensions
# Rank: 7 kyu
# Solved: 2026-05-10
# Source: https://www.codewars.com/kata/euclidean-distance-in-n-dimensions
# -----------------------------------------------

def euclidean_distance(point1, point2):
    return round(sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5, 2)