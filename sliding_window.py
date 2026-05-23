"""
use the Sliding Window algorithm to find the smallest substring in which no letter is repeated more than once.
"""


def max_length_substring_one_repetition(s):
    l, r = 0, 0
    counter = {}

    counter[s[0]] = 1
    _max = 1

    while r < len(s) - 1:
        r += 1

        if counter.get(s[r]):
            counter[s[r]] += 1
        else:
            counter[s[r]] = 1

        while counter[s[r]] == 3:
            counter[s[l]] -= 1
            l += 1
        _max = max(_max, r - l + 1)

    return _max


a = "bcbbbcba"
b = "b"

print(max_length_substring_one_repetition(a))
print(max_length_substring_one_repetition(b))
