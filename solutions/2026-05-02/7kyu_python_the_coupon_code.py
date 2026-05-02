# Kata: The Coupon Code
# Rank: 7 kyu
# Solved: 2026-05-02
# Source: https://www.codewars.com/kata/the-coupon-code
# -----------------------------------------------

from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code == correct_code and type(entered_code) is type(correct_code):
        date_format = "%B %d, %Y"
        current = datetime.strptime(current_date, date_format)
        expiration = datetime.strptime(expiration_date, date_format)
        return current <= expiration
    return False