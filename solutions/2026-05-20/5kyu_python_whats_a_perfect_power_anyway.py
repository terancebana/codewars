# Kata: What's a Perfect Power  anyway?
# Rank: 5 kyu
# Solved: 2026-05-20
# Source: https://www.codewars.com/kata/whats-a-perfect-power-anyway
# -----------------------------------------------

MCP issues detected. Run /mcp list for status.import math

def isPP(n):
    for k in range(2, int(math.log(n, 2)) + 1):
        m = round(n**(1.0 / k))
        if m**k == n:
            return [m, k]
    return None