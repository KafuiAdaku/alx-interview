#!/usr/bin/python3
"""validUTF8 module"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid utf-8 encoding
    Args:
        data (list): A list of integers

    Returns (boolean): True or False
    """
    byte = 0

    if not data:
        return False

    for character in data:
        if byte == 0:
            if ((character >> 3) & 0b111) == 0b110:
                byte = 2
            elif ((character >> 4) & 0b1111) == 0b1110:
                byte = 3
            elif ((character >> 5) & 0b11111) == 0b11110:
                byte = 4
            elif (character >> 7) == 0:  # and character <= 127:
                # byte = 0
                continue
            else:
                return False
        else:
            if (character & 0b11000000) == 0b10000000:
                byte -= 1
            else:
                return False

    if byte != 0:
        return False

    return True
