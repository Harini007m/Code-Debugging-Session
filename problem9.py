# Problem9: Return all possible subsets of a list of unique elements.

def subsets(nums):
    result = [[]]
    for num in nums:
        for subset in result[:]:
            result.append(subset + [num])
    return result

print(subsets([1,2,3]))
