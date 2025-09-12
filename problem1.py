# Problem1: Given a list of integers, return the sum of all even numbers.

def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
