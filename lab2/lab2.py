import math


def banana_and_jackie(piles, H):
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        hours_needed = sum(math.ceil(p / mid) for p in piles)

        if hours_needed <= H:
            right = mid
        else:
            left = mid + 1

    return left

