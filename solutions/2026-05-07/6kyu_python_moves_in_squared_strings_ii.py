# Kata: Moves in squared strings (II)
# Rank: 6 kyu
# Solved: 2026-05-07
# Source: https://www.codewars.com/kata/moves-in-squared-strings-ii
# -----------------------------------------------

def rot(strng):
    return strng[::-1]

def selfie_and_rot(strng):
    n = len(strng.split('\n')[0])
    dots = "." * n
    s1 = "\n".join(line + dots for line in strng.split('\n'))
    s2 = "\n".join(dots + line for line in rot(strng).split('\n'))
    return s1 + "\n" + s2

def oper(fct, s):
    return fct(s)