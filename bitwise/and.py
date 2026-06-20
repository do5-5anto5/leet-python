"""
The bitwise AND operator '&' evaluates the bits at each position.
It returns a new integer where each bit is set to 1 only if both corresponding bits are 1.

Example:
5 = 101 (binary)
5 & 1 = 1  --> 101 & 001: only the last bit matches as 1, returning 1.
5 & 5 = 5  --> 101 & 101: all bits are identical, returning 5.
"""

print(f'5: {bin(5)} & 13: {bin(13)}')
print(5 & 13)  # 101 & 1101 returns 101

print(f'12: {bin(12)} & 13: {bin(13)}')
print(12 & 13)  # 1100 & 1101 returns 1100
