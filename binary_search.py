"""
Given an array, this algorithm search a number with log(n) scale
"""


def binary_search(nums, n):
    steps = 0
    lo = 0
    hi = len(nums)

    while lo < hi:
        steps += 1
        mid = int((lo + hi) / 2)

        if nums[mid] == n:
            print('step', steps)
            return mid
        elif mid < n:
            lo = mid + 1
        else:
            hi = mid

    return -1


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ,21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30 ,31 ,32 ,34 ,35 ,36 ,37 ,38 ,39 , 40]
z = [1,2]

print(binary_search(a, 3))
print(binary_search(b, 3))
print(binary_search(d, 3))
print(binary_search(z, 3))
print(binary_search(z, 2))
