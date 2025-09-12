# Problem3: Check if two strings are anagrams (contain the same letters in any order).

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))
