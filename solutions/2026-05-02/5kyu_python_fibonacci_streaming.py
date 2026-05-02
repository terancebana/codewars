# Kata: Fibonacci Streaming
# Rank: 5 kyu
# Solved: 2026-05-02
# Source: https://www.codewars.com/kata/fibonacci-streaming
# -----------------------------------------------

def all_fibonacci_numbers():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b