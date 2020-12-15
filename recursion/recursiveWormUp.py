# 1) Calculate the cumulative sum
def rec_sum(n):

    # Base Case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)


# 2) Return the sum of all individual digits in that integer
def sum_func(n):

    # Base Case
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n/10)





























