import math

SNAFU_TO_DECIMAL_MAPPING = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
DECIMAL_TO_SNAFU_MAPPING = {str(v): k for k, v in SNAFU_TO_DECIMAL_MAPPING.items()}


def solve(snafu_numbers) -> str:
    decimal = sum(map(snafu_to_decimal, snafu_numbers))
    return decimal_to_snafu(decimal)


def snafu_to_decimal(snafu_number):
    decimal = 0
    power = len(snafu_number) - 1
    for snafu in snafu_number:
        decimal += SNAFU_TO_DECIMAL_MAPPING[snafu] * int(math.pow(5, power))
        power -= 1
    return decimal


def decimal_to_snafu(decimal):
    base_5 = list(to_base_5(decimal))
    for i in reversed(range(len(base_5))):
        if base_5[i] in ("3", "4", "5"):
            base_5[i - 1] = str(int(base_5[i - 1]) + 1)
            base_5[i] = -5 + int(base_5[i])
    return "".join(DECIMAL_TO_SNAFU_MAPPING[str(d)] for d in base_5)


def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return s
