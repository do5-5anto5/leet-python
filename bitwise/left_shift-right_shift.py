"""
number 100 is represented by 1100100 in bits
shifting it right results 110010 that is equal to 50
shifting it left results 1100100 that is equal to 200
"""

a = bin(100)
print(a)  # 0b1100100

res = 100 >> 1  # 50 | 110010
print(res)  # 50

res = 100 << 1 # 1100100 shift left = 1100100  | 200
print(res)
