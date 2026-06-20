"""
The bitwise operator XOR '^' evaluates the bits at each position.
It returns a new integer where a bit is set to 1
only if the corresponding bits differ (one is 1 and the other is 0).
"""

print(f'5: {bin(5)} ^ 13: {bin(13)}')
print(5 ^ 13)  # 0101 & 1101 returns 1000

print(f'13: {bin(13)} ^ 13: {bin(13)}')
print(13 ^ 13)  # 1101 & 1101 returns 0
# a number XORed itself allways returns 0
