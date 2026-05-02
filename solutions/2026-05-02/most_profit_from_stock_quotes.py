# Kata: Most profit from stock quotes
# Rank: 6 kyu
# Solved: 2026-05-02
# Source: https://www.codewars.com/kata/most-profit-from-stock-quotes
# -----------------------------------------------

def get_most_profit(quotes):
    total_profit = 0
    max_so_far = 0
    for quote in reversed(quotes):
        if quote > max_so_far:
            max_so_far = quote
        else:
            total_profit += max_so_far - quote
    return total_profit