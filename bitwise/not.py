"""
The bitwise NOT operator '~' inverts all the bits of an integer.
It flips every 1 to 0 and every 0 to 1, effectively returning -(x + 1)
due to two's complement representation.
"""

bits = 5
print('5: ', bin(bits))

bits = ~bits
print(bits)

