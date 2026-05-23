def find_error_nums(nums):

    """find and return duplicate and missing numbers"""
    
    duplicate = None
    missing = None

    for i in range(1, len(nums)):
        current = nums[i]
        previous = nums[i - 1]

        if current == previous:
            duplicate = current
        elif current - previous > 1:
            missing = previous + 1

        # border cases
        if missing is None:
            if nums[0] != 0:
                missing = 1
            else:
                missing = len(nums)

    return [duplicate, missing]


print(find_error_nums([2,2]))
print(find_error_nums([1,2,4,4]))