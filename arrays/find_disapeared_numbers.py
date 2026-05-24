def find_disapeared_numbers(nums):

    """find what numbers is not in a sequence"""

    setA = set(nums)
    setB = set()

    for i in range(1, len(nums) + 1):
        setB.add(i)

    result = list(setB.difference(setA))

    return result


print(find_disapeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_disapeared_numbers([1, 1]))
