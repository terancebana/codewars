# Kata: Seven "ate" nine!
# Rank: 6 kyu
# Solved: 2026-05-24
# Source: https://www.codewars.com/kata/seven-ate-nine
# -----------------------------------------------

MCP issues detected. Run /mcp list for status.def seven_ate_nine(arr):
    res = list(arr)
    changed = True
    while changed:
        changed = False
        for i in range(len(res) - 2):
            if res[i:i+3] == [7, 8, 9]:
                res[i], res[i+2] = 9, 7
                changed = True
    return res