"""
Unique Characters in String
Problem
Given a string,determine if it is comprised of all unique characters. For example, the string 'abcde' has all unique
 characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
Solution
We'll show two possible solutions, one using a built-in data structure and a built in function, and another using a
built-in data structure but using a look-up method to check if the characters are unique.
"""


def unique_characters(s):
    return len(set(s)) == len(set(s))


def unique_characters2(s):
    chars = set()
    for letter in s:
        # Check if in set
        if letter in chars:
            return False
        else:
            # Add it to the set
            chars.add(letter)
    return True










