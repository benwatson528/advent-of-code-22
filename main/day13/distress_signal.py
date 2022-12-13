import json
from functools import cmp_to_key


def solve_pairs(packets) -> int:
    right_orders = set()
    for i in range(0, len(packets), 2):
        if compare(packets[i], packets[i + 1]) in (0, -1):
            right_orders.add((i // 2) + 1)
    return sum(right_orders)


def solve_all(packets) -> int:
    ordered = sorted(packets, key=cmp_to_key(compare))
    return (ordered.index(json.loads("[[2]]")) + 1) * (ordered.index(
        json.loads("[[6]]")) + 1)


def compare(left, right):
    is_left_int = isinstance(left, int)
    is_right_int = isinstance(right, int)

    if is_left_int and not is_right_int:
        return compare([left], right)
    elif not is_left_int and is_right_int:
        return compare(left, [right])
    elif is_left_int and is_right_int:
        return compare_ints(left, right)
    else:
        for i in range(len(left)):
            if i >= len(right):
                return 1
            comparison = compare(left[i], right[i])
            if comparison != 0:
                return comparison
        return compare(len(left), len(right))


def compare_ints(left, right):
    if left < right:
        return -1
    elif left == right:
        return 0
    else:
        return 1
