"""
Using Comprehension to solve this algorithm is not actually efficient.
It creates many arrays in the process,
so the spatial complexity does not compare to the standard implementation,
which is 'more manual'.

This implementation is only valid if you don't remember the standard implementation,
but you need to show that you understand what the Quicksort algorithm is.
"""

def quicksort_w_c(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        bigger_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort_w_c(less_than_pivot) + [pivot] + quicksort_w_c(bigger_than_pivot)


nums = [0, 3, 6, 7, 8, 4, 2, 1, 5]
result = quicksort_w_c(nums)

print(result)
