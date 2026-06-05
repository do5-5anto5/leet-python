"""
BUBBLE SORT
    - Time complexity
        - Best case: O(n)
        - Worst case: o(n^2)
    - Space complexity: O(1)

    Inefficient in terms of time complexity.
    But it doesn't need to allocate any memory and doesn't use any extra data structures.

    Historically, at some point it may have been the best algorithm.
    Back when computers used magnetic tape to store data.
"""

def bubble_sort(nums):
    size = len(nums)
    for _ in nums:
        is_sorted = True
        print(nums)
        for i in range(size-1):
            if nums[i] > nums[i+1]:
                is_sorted =False
                nums[i], nums[i+1] = nums[i+1], nums[i]
        if is_sorted:
            return

bubble_sort([5,4,3,2,1])
bubble_sort([1,2,3,4,5])
