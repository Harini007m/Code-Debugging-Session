# Problem7: Given an array containing n distinct numbers from 0 to n, find the missing number.

def find_missing(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(find_missing([3, 0, 1]))
