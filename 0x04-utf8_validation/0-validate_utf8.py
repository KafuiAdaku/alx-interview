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

    for character in data:
        bin_num = "{:08b}".format(character & 0b11111111)
        if byte == 0:
            for bit in bin_num:
                if bit == '0':
                    break
                byte += 1
            if byte == 0:
                continue
            if byte == 1 or byte > 4:
                return False
        else:
            if not (bin_num[0] == '1' and bin_num[1] == '0'):
                return False
        byte -= 1
    return byte == 0
