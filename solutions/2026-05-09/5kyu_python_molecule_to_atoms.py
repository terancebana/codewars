# Kata: Molecule to atoms
# Rank: 5 kyu
# Solved: 2026-05-09
# Source: https://www.codewars.com/kata/molecule-to-atoms
# -----------------------------------------------

import re
from collections import Counter

def parse_molecule(formula):
    formula = formula.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')')
    tokens = re.findall(r'([A-Z][a-z]?|\(|\)|\d+)', formula)
    stack = [Counter()]
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '(':
            stack.append(Counter())
            i += 1
        elif token == ')':
            i += 1
            multiplier = 1
            if i < len(tokens) and tokens[i].isdigit():
                multiplier = int(tokens[i])
                i += 1
            top = stack.pop()
            for atom, count in top.items():
                stack[-1][atom] += count * multiplier
        else:
            atom = token
            i += 1
            multiplier = 1
            if i < len(tokens) and tokens[i].isdigit():
                multiplier = int(tokens[i])
                i += 1
            stack[-1][atom] += multiplier
    return dict(stack[0])