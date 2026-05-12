# Kata: FizzBuzz++
# Rank: 6 kyu
# Solved: 2026-05-12
# Source: https://www.codewars.com/kata/fizzbuzz-plus-plus
# -----------------------------------------------

def fizzbuzz_plusplus(numbers, words):
    product = 1
    for n in numbers:
        product *= n
    
    result = []
    for i in range(1, product + 1):
        s = "".join(word for num, word in zip(numbers, words) if i % num == 0)
        result.append(s if s else i)
    return result