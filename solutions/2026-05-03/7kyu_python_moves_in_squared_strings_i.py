# Kata: Moves in squared strings (I)
# Rank: 7 kyu
# Solved: 2026-05-03
# Source: https://www.codewars.com/kata/moves-in-squared-strings-i
# -----------------------------------------------

def vert_mirror(strng):
    return "\n".join(line[::-1] for line in strng.split("\n"))

def hor_mirror(strng):
    return "\n".join(strng.split("\n")[::-1])

def oper(fct, s):
    return fct(s)