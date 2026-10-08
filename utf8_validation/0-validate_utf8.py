#!/usr/bin/python3
"""Validate whether a sequence of integers encodes valid UTF-8."""


def validUTF8(data):
    """Check whether the integers in data form a valid UTF-8 sequence.

    Args:
        data: An iterable of integers. Only the lowest 8 bits of each
            integer are examined.

    Returns:
        True if data is a valid UTF-8 sequence; otherwise, False.
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            for i in range(7, -1, -1):
                if (byte >> i) & 1:
                    num_bytes += 1
                else:
                    break

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if (byte >> 6) != 0b10:
                return False

        num_bytes -= 1

    return num_bytes == 0
