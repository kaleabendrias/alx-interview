#!/usr/bin/python3
"""a script that checks if it is valid utf-8"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers, each representing a byte of data.

    Returns:
        True if the data is a valid UTF-8 encoding, False otherwise.
    """

    num_bytes_remaining = 0

    for num in data:
        if num_bytes_remaining == 0:
            # Check for single-byte characters
            if (num >> 7) == 0:
                continue

            # Check for multi-byte characters
            leading_ones = 0
            while num & (1 << 7):  # Count leading 1 bits
                leading_ones += 1
                num <<= 1

            if not (2 <= leading_ones <= 4):
                return False  # Invalid leading byte

            num_bytes_remaining = leading_ones - 1
        else:
            # Check for continuation bytes
            if not (num >> 6) == 0b10:
                return False

        num_bytes_remaining -= 1

    return num_bytes_remaining == 0
