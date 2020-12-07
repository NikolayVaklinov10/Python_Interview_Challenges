"""
It's worthwhile at this point to explain that Big O can be used to determine three cases with an algorithm:

        * Best Case: In the telephone book search, the best case is that we find the name in one comparison.
        This is O(1) or constant complexity;

        * Expected Case: As discussed above this is O(log n); and

        * Worst Case: This is also O(log n).
"""


# O(n)
def my_function(n):
    for x in range(n):
        print(x)


# O(n2)
def my_function2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)








