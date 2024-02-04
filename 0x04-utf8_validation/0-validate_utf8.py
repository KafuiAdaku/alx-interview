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
    #         if ((character >> 3) & 0b111) == 0b110:
    #             byte = 2
    #         elif ((character >> 4) & 0b1111) == 0b1110:
    #             byte = 3
    #         elif ((character >> 5) & 0b11111) == 0b11110:
    #             byte = 4
    #         elif (character >> 7) == 0:  # and character <= 127:
    #             # byte = 0
    #             continue
    #         else:
    #             return False
    #     else:
    #         if (character & 0b11000000) == 0b10000000:
    #             byte -= 1
    #         else:
    #             return False

    # if byte != 0:
    #     return False

    # return True
