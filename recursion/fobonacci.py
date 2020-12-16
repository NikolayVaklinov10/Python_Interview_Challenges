

def fibonacci(n):

    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


"""
UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
THEN RUN THE CELL.
"""

from nose.tools import assert_equal


class TestFib(object):

    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(1), 1)
        assert_equal(solution(23), 28657)
        print('Passed all tests.')


# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

t.test(fibonacci)
# t.test(fib_dyn) # Note, will need to reset cache size for each test!
# t.test(fib_iter)

