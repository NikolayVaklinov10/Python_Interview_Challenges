
def solution(lst, target):

    seen = set()

    for num in lst:

        num2 = target - num

        if num2 in seen:
            return True

        seen.add(num)

    return False



