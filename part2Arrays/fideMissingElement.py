"""
Find the Missing Element
Problem
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
Input:
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
5 is the missing number
"""


def finder(arr1, arr2):

    # Sort the arrays
    arr1.sort()
    arr2.sort()

    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    # Otherwise return last element
    return arr1[-1]


"""
A linear solution
"""
import collections


def finder2(arr1, arr2):

    # Using default dict to avoid key errors
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    # Check if num not in dictionary
    for num in arr1:
        if d[num] == 0:
            return num

        # Otherwise, subtract a count
        else:
            d[num] -= 1


"""
Another way to solve the challenge with finding the excluded value
"""


def finder3(arr1, arr2):
    result = 0

    # Perform an XOR between
    for num in arr1+arr2:
        result ^= num
        print(result)

    return result






