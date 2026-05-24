"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


def reverse_words_in_a_string(s: str) -> str:
    res = ""
    l, r = 0, 0

    while r < len(s):
        if s[r] != " ":
            r += 1
        else:
            res += s[l : r + 1][::-1]
            r += 1
            l = r

    res += " " + s[l : r +2][::-1]

    return res[1:]


result = reverse_words_in_a_string("car tra")

print(result)
