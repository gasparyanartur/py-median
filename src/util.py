import math


def count_items(items, max_val=None):
    if len(items) == 0:
        return []

    if max_val is None:
        max_val = max(items)

    counts = [0 for _ in range(max_val+1)]
    for item in items:
        counts[item] += 1
    
    return counts


def get_median(counts):
    n = sum(counts)

    if n == 0:
        return None

    if n == 1:
        return 0
    
    if (n % 2) == 0:
        return get_median_even(counts, n)

    return get_median_odd(counts, n)


def get_median_odd(counts, n):
    mid = n / 2
    index = 0

    for bin, count in enumerate(counts):
        index += count

        if index >= mid:
            return bin

    return None

    
def get_median_even(counts, n):
    mid = (n - 1) / 2
    target_lo = math.floor(mid)
    target_hi = math.ceil(mid)

    lo_bin = -1
    hi_bin = -1
    index = 0

    for bin, count in enumerate(counts):
        index += count

        if (lo_bin == -1) and (index >= target_lo):
            lo_bin = bin

        if (hi_bin == -1) and (index >= target_hi):
            hi_bin = bin

        if (lo_bin != -1) and (hi_bin != -1):
            return (lo_bin + hi_bin) / 2

    return None


