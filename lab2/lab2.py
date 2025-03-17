import math


def banana_and_jackie(piles, H):
    left, right = 1, max(piles)

    while left < right:
        ser = (left + right) // 2
        hours_needed = sum(math.ceil(el / ser) for el in piles)

        if hours_needed <= H:
            right = ser
        else:
            left = ser + 1

    return left

