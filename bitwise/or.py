"""
The bitwise operator OR '|' evaluates the bits at each position.
It returns a new integer where a bit is set to 1
if at least one of the corresponding bits is 1.
"""

print(f'5: {bin(5)} | 13: {bin(13)}')
print(5 | 13)  # 101 & 1101 returns 1101

print(f'12: {bin(12)} | 13: {bin(13)}')
print(12 | 13)  # 1100 & 1101 returns 1101