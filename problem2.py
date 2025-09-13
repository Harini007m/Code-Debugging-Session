# Problem2: Return the second largest unique number in the list.

def second_largest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([4, 1, 7, 7, 3]))
